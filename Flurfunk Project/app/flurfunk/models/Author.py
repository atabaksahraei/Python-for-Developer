class Author():
    def __init__(self):
        self.name = None

# for np.unique
    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name