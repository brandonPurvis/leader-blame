import pickle
import git
import os
import time

# Create your models here.
class LeaderBoard(object):
    def __init__(self):
        self.authors = []
        self._load_authors()
        self._load_files()

    def _load_authors(self):
        with open('./blame/data/data.p') as data_file:
            authors = pickle.load(data_file)
        for author in authors:
            self.authors.append(Author(author))

    def _load_files(self):
        with open('./blame/data/info.p') as data_file:
            self.files = pickle.load(data_file)

    def sort(self):
        self.authors.sort(key=lambda x: len(x.commits), reverse=True)
        return self.authors

class Repo(object):
    def __init__(self):
        self.authors = []
        self.repo = git.Repo("./blame/osf.io")

    def getfilePath(self,requested_filename):
        paths = []
        for x in self.repo.index.entries:
            paths.append(x[0])


        for filename in paths:
            if filename.endswith(requested_filename):
                file_index = filename

        print(file_index)
        return file_index

    def blame(self,file_index):
        info = {}
        retval = '<table width="100%">'
        for commit, lines in self.repo.blame('HEAD', file_index):
            for line in lines:
                line = line.replace("<", "&lt;")
                line = line.replace(">", "&gt;")
                line = line.replace(" ", "&nbsp")
                retval += '<tr>'
                retval += '<td >' +str(line.encode('ascii', 'ignore'))+ '</td><td>'+ "  " + commit.author.name.encode('ascii', 'ignore')+"</td><td>-" + str(time.asctime(time.gmtime(commit.committed_date))) + " "  + '</td>'
                retval += '</tr>'

        retval += "</table>"
        retval += "<hr>"

        return retval



class Author(object):
    def __init__(self, dict):
        self.name = dict['name']
        self.commits = dict['commits']
        self.commitsNum = len(dict['commits'])

    def print_commits(self):
        for lines in self.commits:
            print lines

Repo()