from django.shortcuts import render
from django.http import HttpResponse

from load import LeaderBoard, Author

import git
import time
import os
# Create your views here.
def index(request):
    return render(request, 'blame.html')

def leaderboard(request):
    retval = '<table>'
    LB = LeaderBoard()
    LB.loadAuthors()
    LB.sort()
    retval += "<thead><b>"
    retval += "<td> Author Name</td>"
    retval += "<td> Number of Commits</td>"
    retval += "</b></thead>"

    for author in LB.authors:
        retval += "<tr>"
        retval += "<td>" + author.name + "</td>"
        retval += "<td>" + str(author.commitsNum) + "</td>"
        retval += "</tr>"

    retval += "</table>"

    return HttpResponse(retval)


def blame(request):

    LB = LeaderBoard()
    LB.loadFiles()
    LB.loadAuthors()

    retval = "<h1>" + request.POST.get('textfield', None) + "</h1>"
    retval += '<table width="100%">'

    authors = []
    authorDict = {}

    for key, value in LB.files.iteritems():
        if key.endswith(request.POST.get('textfield', None)):
            inx = key


    try:
        retval += LB.files[inx]
    except:
        retval = "You spelled it wrong"
    return HttpResponse(retval)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

