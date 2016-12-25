class Action(object):
    actions = {}

    def __init__(self, name, term):
        self.name = name
        self.term = term
        self.__class__.actions[term] = self

    @classmethod
    def get_actions(cls):
        return cls.actions

    @classmethod
    def map(cls, term):
        return cls.actions[term].name

    @classmethod
    def create_many(cls, naming, tokens):
        for i, name in enumerate(naming):
            cls(name, tokens[i])
