from django.shortcuts import render_to_response
from blame.utils.load import LeaderBoard
from blame.forms import QueryForm


def index(request):
    context = {}
    form = QueryForm()
    context.update({'form': form})
    return render_to_response('blame.html', context)


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
    return render_to_response('results.html', context=context)


def leaderboard(request):
    lb = LeaderBoard()
    lb.sort()
    context = {}
    context.update({'authors': lb.authors})
    return render_to_response('leaderboard.html', context=context)
