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
            if file.endswith(".js") or file.endswith(".py") :
                 dirdict[file] = os.path.join(root, file)[10:]
    repo = git.Repo("../osf.io")

    retval = "<h1>" + dirdict[request.POST.get('textfield', None)] + "</h1>"
    retval += '<table width="100%">'

    authors = []

    for commit, lines in repo.blame('HEAD', dirdict[request.POST.get('textfield', None)]):
        for line in lines:
            if commit.author not in authors:
                authors.append(commit.author)

            line = line.replace(" ", "&nbsp")
            retval += '<tr>'
            retval += '<td >' +str(line)+ '</td><td>' + str(commit.author) + '</td>'
            retval += '</tr>'

    retval += "<h2>Authors</h2>"
    for author in authors:
        retval += "<dd>"+ str(author)

    retval += "<hr>"


    return HttpResponse(retval)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

