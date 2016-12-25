class Object(object):
    objects = {}

    def __init__(self, name, term):
        self.name = name
        self.term = term
        self.__class__.objects[term] = self

    @classmethod
    def get_objects(cls):
        return cls.objects

    @classmethod
    def map(cls, term):
        return cls.objects[term].name

    @classmethod
    def create_many(cls, naming, tokens):
        for i, name in enumerate(naming):
            cls(name, tokens[i])
