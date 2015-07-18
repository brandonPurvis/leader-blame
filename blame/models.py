import pickle

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


class Author(object):
    def __init__(self, dict):
        self.name = dict['name']
        self.commits = dict['commits']
        self.commitsNum = len(dict['commits'])

    def print_commits(self):
        for lines in self.commits:
            print lines
