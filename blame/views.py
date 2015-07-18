from django.http import HttpResponse
from django.template import RequestContext, loader
from blame.models import LeaderBoard, Repo
from blame.forms import QueryForm


def render(request, template_name, context=None):
    template = loader.get_template(template_name)
    context = context or {}
    context = RequestContext(request, context)
    response = HttpResponse(template.render(context))
    return response

def index(request):
    context = {}
    form = QueryForm()
    context.update({'form': form})
    return render(request, 'blame.html', context)


def getRepo(request):
    context = {}
    return render(request, 'getRepo.html', context=context)


def blame(request):
    context = {}
    repo = Repo()
    form = QueryForm(request.POST)

    file_index = None

    form.is_valid()
    requested_filename = form.cleaned_data['query']

    filePath = repo.getfilePath(requested_filename)
    file_contents = repo.blame(filePath)
    context.update({'file_name': filePath})
    context.update({'file_contents': file_contents})
    return render(request, 'results.html', context=context)


def leaderboard(request):
    lb = LeaderBoard()
    lb.sort()
    context = {}
    context.update({'authors': lb.authors})
    return render(request, 'leaderboard.html', context=context)
