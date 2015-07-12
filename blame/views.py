from django.shortcuts import render
from blame.utils.load import LeaderBoard


def index(request):
    return render(request, 'blame.html')


def blame(request):
    lb = LeaderBoard()
    requested_filename = request.POST.get('textfield', 'invalid_request')
    context = {}
    file_index = None
    for filename, value in lb.files.iteritems():
        if filename.endswith(requested_filename):
            file_index = filename

    context.update({'file_name': requested_filename})
    context.update({'file_contents': lb.files[file_index]})
    return render(request, 'results.html', context=context)
