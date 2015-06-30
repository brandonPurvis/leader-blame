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
    repo = git.Repo("../osf.io")
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



files = getFiles()
authors = getBlame(files)
import ast
i = 0

with open('data.txt', 'wb') as outfile:
    pickle.dump(authors, outfile)