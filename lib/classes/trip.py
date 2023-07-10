
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
    
    #property stuff
    def get_visitor( self ):
        return self._visitor 
    
    def set_visitor( self, visitor ):
        if isinstance(visitor, Visitor):
            self._visitor = visitor 
        else:
            raise Exception("Visitor must be a Visitor object")
    
    visitor = property( get_visitor, set_visitor )
            
