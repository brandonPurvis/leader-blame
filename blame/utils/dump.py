__author__ = 'johntordoff'
import git
import time
import os
import pickle
import json as simplejson

class Author():
    def __init__(self,name=None):
        self.commits = []
        self.name = name

class Commit():
    def __init__(self,commit,lines):
        self.lines = lines
        self.author = commit.author
        del commit

def getFiles():
    repoDir = "../osf.io"
    newfiles = []
    for root, dirs, files in os.walk(repoDir):
        for file in files:
            if file.endswith(".js") or file.endswith(".py") or file.endswith(".mako") :
                newfiles.append(os.path.join(root, file).replace(repoDir+"/", ''))

    return newfiles

def getBlame(files):

    authors = []
    repo = git.Repo("/Users/johntordoff/osf.io")
    i = 0
    for file in files:
        try:
            for commit, lines in repo.blame('HEAD',file ):
                commit = Commit(commit,lines)
                if commit.author.name not in [x.name for x in authors]:
                    author = Author(commit.author.name)
                    authors.append(author)
                author = [x for x in authors if x.name == commit.author.name][0]
                author.commits.append(commit)
        except:
            print file
    i = 0
    for author in authors:
        j = 0
        for commit in author.commits:
            del commit.author
            author.commits[j] = commit.__dict__
            j+=1
        authors[i] = author.__dict__

        i +=1

    return authors

def dumpBlame():
    dirdict = {}
    repoDir = "/Users/johntordoff/osf.io"
    indexedFiles = []
    repo = git.Repo(repoDir)

    import os
    for root, dirs, files in os.walk(repoDir):
        for file in files:
            if file.endswith(".js") or file.endswith(".py") or file.endswith(".mako") :
                print os.path.join(root, file)
                indexedFiles.append(os.path.join(root, file))

    authors = []
    authorDict = {}

    print len(indexedFiles)
    info = {}

    for file in indexedFiles:
        info[file] = ''
        retval = ''
        print indexedFiles.index(file)
        try:
            for commit, lines in repo.blame('HEAD', file):
                for line in lines:
                    line = line.replace("<", "&lt;")
                    line = line.replace(">", "&gt;")
                    line = line.replace(" ", "&nbsp")
                    retval += '<tr>'
                    retval += '<td >' +str(line.encode('ascii', 'ignore'))+ '</td><td>'+ "  " + commit.author.name.encode('ascii', 'ignore')+"</td><td>-" + str(time.asctime(time.gmtime(commit.committed_date))) + " "  + '</td>'
                    retval += '</tr>'

            retval += "<hr>"
            info[file] = retval
        except:
            info[file] = "Mea Blamea"

    with open('info.p', 'wb') as outfile:
        pickle.dump(info, outfile)
