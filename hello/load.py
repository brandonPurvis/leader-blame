import json

class LeaderBoard():
    def __init__(self):
        self.authors = []

    def load(self):
        with open('data.txt') as data_file:
            authors = json.load(data_file)

        for author in authors:
            self.authors.append(Author(author))

    def sort(self):
        self.authors.sort(key=lambda x: len(x.commits), reverse=True)
        return self.authors

class Author():
    def __init__(self,dict):
        self.name = dict['name']
        self.commits = dict['commits']
        self.commitsNum = len(dict['commits'])


