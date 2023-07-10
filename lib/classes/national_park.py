class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    #property stuff
    def get_name( self ):
        return self._name 
    
    def set_name( self, name ):
        if not hasattr( self, 'name' ):
            self._name = name
        else:
            raise Exception("Name already set.")

    name = property( get_name, set_name )

    #other stuff        
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