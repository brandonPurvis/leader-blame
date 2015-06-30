from django.shortcuts import render
from django.http import HttpResponse

from load import LeaderBoard

import git
import time
import os
# Create your views here.
def index(request):
    LB = LeaderBoard()
    LB.load()
    LB.sort()

    return render(request, 'blame.html', {'authors': LB.authors})


def blame(request):
    dirdict = {}
    repoDir = "./osf.io"

    import os
    for root, dirs, files in os.walk(repoDir):
        for file in files:
            if file.endswith(".js") or file.endswith(".py") or file.endswith(".mako") :
                dirdict[file] = os.path.join(root, file).replace(repoDir+"/", '')
    repo = git.Repo(repoDir)

    retval = "<h1>" + dirdict[request.POST.get('textfield', None)] + "</h1>"
    retval += '<table width="100%">'

    authors = []
    authorDict = {}

    for commit, lines in repo.blame('HEAD', dirdict[request.POST.get('textfield', None)]):
        if commit.author.name not in authors:
            authors.append(commit.author.name)
            authorDict[commit.author.name] = 1
        else:
            authorDict[commit.author.name] += 1

    for commit, lines in repo.blame('HEAD', dirdict[request.POST.get('textfield', None)]):
        for line in lines:
            if request.POST.get('textfield', None)[-4:] == 'mako':
                line = line.replace("<", "&lt;")
                line = line.replace(">", "&gt;")
            line = line.replace(" ", "&nbsp")
            retval += '<tr>'
            retval += '<td >' +str(line.encode('ascii', 'ignore'))+ '</td><td>'+ "  " + commit.author.name.encode('ascii', 'ignore')+"</td><td>-" + str(time.asctime(time.gmtime(commit.committed_date))) + " "  + '</td>'
            retval += '</tr>'


    retval += "<h2>Authors</h2>"
    for author in authors:
        retval += "<dd>"+ author + " : " + str(authorDict[author])

    retval += "<hr>"


    return HttpResponse(retval)


def author(request):
    files = aggrate.getFiles()
    authors = aggrate.getBlame(files)
    retval = ""

    for author in authors:
        retval += author.name + "<br>"

    return HttpResponse(retval)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

