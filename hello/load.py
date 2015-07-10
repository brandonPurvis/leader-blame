import json
import pickle

class LeaderBoard():
    def __init__(self):
        self.authors = []

    def loadAuthors(self):
        with open('./data.p') as data_file:
            authors = pickle.load(data_file)

        for author in authors:
            self.authors.append(Author(author))

    def loadFiles(self):
        with open('./info.p') as data_file:
            self.files = pickle.load(data_file)

    def sort(self):
        self.authors.sort(key=lambda x: len(x.commits), reverse=True)
        return self.authors

class Author():
    def __init__(self,dict):
        self.name = dict['name']
        self.commits = dict['commits']
        self.commitsNum = len(dict['commits'])

    def printCommit(self):
        for lines in self.commits:
            print lines

