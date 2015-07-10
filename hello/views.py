from django.shortcuts import render
from django.http import HttpResponse

from load import LeaderBoard, Author

import git
import time
import os
# Create your views here.
def index(request):
    LB = LeaderBoard()
    LB.loadAuthors()
    LB.sort()

    return render(request, 'blame.html',  {"authors" : LB.authors})


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

    print( inx)
    retval += LB.files[inx]

    return HttpResponse(retval)


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

