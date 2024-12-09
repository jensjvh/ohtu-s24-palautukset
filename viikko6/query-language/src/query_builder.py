from matchers import (
    And, 
    HasAtLeast,
    PlaysIn,
    All,
    HasFewerThan,
    Not,
    Or
)


class QueryBuilder:
    def __init__(self):
        self._reset()

    def _reset(self):
        self._matcher = All()

    def plays_in(self, team):
        return self._add_matcher(PlaysIn(team))

    def has_at_least(self, value, attr):
        return self._add_matcher(HasAtLeast(value, attr))

    def has_fewer_than(self, value, attr):
        return self._add_matcher(HasFewerThan(value, attr))

    def has_not(self, matcher):
        return self._add_matcher(Not(matcher))

    def one_of(self, *matchers):
        self._matcher = (Or(*matchers))
        return self

    def _add_matcher(self, matcher):
        self._matcher = And(self._matcher, matcher)
        return self

    def build(self):
        result = self._matcher
        self._reset()
        return result