class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        # VERSION 1
        # counts = {visitor: visitors.count(visitor) for visitor in visitors}
        # sorted_list = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        # return sorted_list[0][0]

        # VERSION 2
        # return Counter(visitors).most_common(1)[0][0]

        # VERSION 3
        return max(set(visitors), key=visitors.count)
    
    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())

from classes.trip import Trip
from collections import Counter