from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import git
import os

# Create your views here.
def index(request):
    return render(request, 'blame.html')


def blame(request):

    dirdict = {}

    import os
    for root, dirs, files in os.walk("../osf.io"):
        for file in files:
            if file.endswith(".py") or file.endswith(".js"):
                 dirdict[file] = os.path.join(root.replace('../osf.io/',''), file)

    repo = git.Repo("../osf.io")
    retval = '<table width="100%">'
    indent = ''

    for commit, lines in repo.blame('HEAD', dirdict[request.POST.get('textfield', None)]):
        
        
        for line in lines:
            line = line.replace(" ", "&nbsp")
            retval += '<tr>'
            retval += '<td ><font size="12">' +str(line)+ '</font></td><td>' + str(commit.author) + '</td>'
            retval += '</tr>'

    return HttpResponse(retval)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

