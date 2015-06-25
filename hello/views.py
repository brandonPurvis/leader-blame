from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import git
import os

# Create your views here.
def index(request):
    return render(request, 'blame.html')


def blame(request):
    repo = git.Repo("../osf.io")
    retval = '<table width="100%">'
    indent = ''
    for commit, lines in repo.blame('HEAD', "website/static/js/"+request.POST.get('textfield', None)):
        
        
        for line in lines:
            line = line.replace(" ", "&nbsp")
            retval += '<tr>'
            retval += '<td >' + indent + str(line)+ '</td><td>' + str(commit.author) + '</td>'
            retval += '</tr>'
            try:
                if line[-1] == "{":
                    indent += "     "
                else:
                    indent = ""
            except:
                pass


    return HttpResponse(retval)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

