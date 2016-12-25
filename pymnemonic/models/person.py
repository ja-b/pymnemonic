class Person(object):
    people = {}

    def __init__(self, name, term):
        self.name = name
        self.term = term
        self.__class__.people[term] = self

    @classmethod
    def get_people(cls):
        return cls.people

    @classmethod
    def map(cls, term):
        return cls.people[term].name

    @classmethod
    def create_many(cls, naming, tokens):
        for i, name in enumerate(naming):
            cls(name, tokens[i])

