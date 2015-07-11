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

    file_index = None
    for filename, value in lb.files.iteritems():
        print('file: {}'.format(filename))
        if filename.endswith(requested_filename):
            file_index = filename

    if file_index:
        response = "<h1>{}</h1><table width=\"100%\">".format(requested_filename)
        response += lb.files[file_index]
        return HttpResponse(response)
    else:
        return HttpResponse("You spelled it wrong")
