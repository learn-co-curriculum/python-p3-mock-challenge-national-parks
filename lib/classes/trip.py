from classes.visitor import Visitor
from classes.national_park import NationalPark
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        
        visitor.trips(self)
        national_park.trips(self)
        
        visitor.national_parks(self.national_park)
        national_park.visitors(self.visitor)
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter 
    def visitor(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else: 
            raise Exception("Not a visitor object")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park): 
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("Not a NationalPark object")