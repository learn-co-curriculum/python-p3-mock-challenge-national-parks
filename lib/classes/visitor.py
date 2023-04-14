class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        pass
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        pass