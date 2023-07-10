from classes.visitor import Visitor
from classes.national_park import NationalPark

class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
<<<<<<< HEAD
    
    #property stuff
    def get_visitor( self ):
        return self._visitor 
    
=======
        Trip.all.append(self)

    def get_visitor( self ):
        return self._visitor 

>>>>>>> 92e4d09ec80c348e44188f28cbd46419b930a503
    def set_visitor( self, visitor ):
        if isinstance(visitor, Visitor):
            self._visitor = visitor 
        else:
            raise Exception("Visitor must be a Visitor object")
<<<<<<< HEAD
    
    visitor = property( get_visitor, set_visitor )
            
=======

    visitor = property(get_visitor, set_visitor)

    def get_national_park(self):
        return self._national_park 
    
    def set_national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("")
        
    national_park = property(get_national_park, set_national_park)
>>>>>>> 92e4d09ec80c348e44188f28cbd46419b930a503
