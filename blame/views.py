from blame import forms
from django.shortcuts import render
from django.http import HttpResponse
from blame.utils.load import LeaderBoard


def index(request):
    return render(request, 'blame.html')


def main_page(request):
    form = forms.SearchForm()
    context = {'form': form}
    return render(request, 'results.html', context=context)


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
