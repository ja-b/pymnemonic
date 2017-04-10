class Domain(object):

    def __init__(self):
        self._detected_set = set()

    def __contains__(self, item):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class NumericDomain(Domain):
    _number_set = range(0, 99)

    def __contains__(self, item):
        if item in self.__class__._number_set:
            return True

    def __iter__(self):
        return iter(self.__class__._number_set)


