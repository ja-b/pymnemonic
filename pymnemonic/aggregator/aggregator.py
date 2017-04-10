class Aggregator(object):

    def aggregate(self, terms):

        raise NotImplementedError


class NaiveAggregator(Aggregator):

    def aggregate(self, terms):

        return " ".join(terms)
