class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    def get_name( self ):
        return self._name 
    
    def set_name( self, name ):
        if not hasattr( self, 'name' ) and type(name) == str:
            self._name = name
        else:
            raise Exception("Name already set.")
        
    name = property(get_name, set_name)
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        trips_list = [x for x in Trip.all if x.national_park == self]
        return trips_list 
    
    def visitors(self, new_visitor=None):
        #don't know why this is here, v
        from classes.visitor import Visitor
        visitor_list = []
        for trip in self.trips():
            if trip.visitor not in visitor_list:
                visitor_list.append(trip.visitor)
        return visitor_list        
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass