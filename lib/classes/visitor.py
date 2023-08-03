class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        pass
    
    def national_parks(self):
        pass
    
    def total_visits_at_park(self, park):
        pass

from classes.trip import Trip
from classes.national_park import NationalPark