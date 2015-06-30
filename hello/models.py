from django.db import models
import os
import git
import time
import os

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class File(models.Model):

    def __init__(self,file):
        dirdict = {}
        repoDir = "./osf.io"

        authors = []

        for commit, lines in repo.blame('HEAD', file):
            if commit.author.name not in authors:
                authors.append(commit.author.name)

class Author():
    def __init__(self,names=None):
        self.commits = []
        self.names = names

    def get_commits(self):
        repoDir = "./osf.io"
        repo = git.Repo(repoDir)

        commits = list(repo.iter_commits('develop'))

        for commit in commits:
            if commit.author.name in self.names:
                self.commits.append(commit)


        return self.commits
