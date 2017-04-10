
class Generator(object):

    def __init__(self, domain):

        self._domain = domain

    def map(self, terms=None):

        raise NotImplementedError

class PersonActionGenerator(object):

    def map(self, terms=None):

        pass