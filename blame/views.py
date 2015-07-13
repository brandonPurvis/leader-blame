from django.http import HttpResponse
from django.template import RequestContext, loader
from blame.utils.load import LeaderBoard
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


def blame(request):
    context = {}
    lb = LeaderBoard()
    form = QueryForm(request.POST)

    file_index = None

    form.is_valid()
    requested_filename = form.cleaned_data['query']

    for filename, value in lb.files.iteritems():
        if filename.endswith(requested_filename):
            file_index = filename

    file_contents = lb.files[file_index] if file_index else 'File does not exist.'
    context.update({'file_name': requested_filename})
    context.update({'file_contents': file_contents})
    return render(request, 'results.html', context=context)


def leaderboard(request):
    lb = LeaderBoard()
    lb.sort()
    context = {}
    context.update({'authors': lb.authors})
    return render(request, 'leaderboard.html', context=context)
