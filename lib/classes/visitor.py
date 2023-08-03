class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        # else:
        #     raise Exception

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        # if not isinstance(park, NationalPark):
        #     raise Exception
        if not park.visitors():
            return 0
        return len([trip for trip in self.trips() if trip.national_park == park])


from classes.trip import Trip
from classes.national_park import NationalPark
