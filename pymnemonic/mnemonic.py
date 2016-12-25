class Mnemonic(object):
    """
    Intended as abstract
    """

    @property
    def term(self):
        raise NotImplementedError

    @term.setter
    def term(self, term):
        raise NotImplementedError

    def process_set(self, term_set):
        """
        Returns a generator that processes each item against Mnemonic
        :param term_set:
        :return:
        """
        return (self.term(term).term for term in term_set)


class PAOMnemonic(Mnemonic):
    """
    Basic implementation of a Person-Action-Object(PAO) Mnemonic
    """

    def __init__(self, person, action, object, token_fn=lambda x: x.split(' ')):

        #Todo Check if models match impl
        self.person = person
        self.action = action
        self.object = object

        self.token_fn = token_fn

    @property
    def term(self):

        return self._term, (self.person, self.action, self.object)

    @term.setter
    def term(self, term):

        self._term = self.token_fn(term)
        self._person = self.term[0]
        self._action = self.term[1]
        self._object = self.term[2]

class SequenceMnemonic(Mnemonic):
    """
    Generic Form of a PAOMnemonic
    """
    pass
