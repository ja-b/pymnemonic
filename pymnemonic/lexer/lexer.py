class Lexer(object):

    def __init__(self, domain, generator, terms):

        self._domain = domain
        self._generator = generator
        self._terms = terms

    def _generate_mapping(self, terms=None):

        self._mapping = self._generator(self._domain).generate(terms=terms)

    def lex(self, data):

        raise NotImplementedError

class NaiveLexer(object):

    def lex(self, data):

        raise NotImplementedError
