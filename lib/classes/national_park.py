class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        pass
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        pass
    
    def total_visits(self):
        pass
    
    def best_visitor(self):
        pass