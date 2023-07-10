class Visitor:

    def __init__(self, name ):
        self.name = name

    #property stuff
    def get_name( self ):
        return self._name

    def set_name( self, name ):
        if (type(name) == str) and (1 <= len(name) <= 15) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("Name should be string between 1 and 15 characters")

    name = property( get_name, set_name ) 
        
    #other stuff
    def trips(self, new_trip=None):
        from classes.trip import Trip
        trips_list = [x for x in Trip.all if x.visitor == self]
        return trips_list
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        np_list = []
        my_trips = self.trips()
        for trip in my_trips:
            if trip.national_park not in np_list:
                np_list.append(trip.national_park)
        return np_list