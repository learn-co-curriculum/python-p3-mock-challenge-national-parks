class NationalPark:
    all = []

    def __init__(self, name):
        self._name = name
        # type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "_name"):
            self._name = name
        # else:
        #     raise Exception 
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)

class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor 
    
    @visitor.setter
    def name(self, visitor):
        if isinstance(visitor, Visitor):
            self._visitor = visitor
    #     # else:
    #     #     raise Exception 
            
    @property 
    def national_park(self):
        return self._national_park
    
    @national_park.setter 
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        # else:
        #     raise Exception

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self,start_date):
        if isinstance(start_date, str) and len(start_date) >= 7:
            self._start_date = start_date
        # else:
        #     raise Exception 
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter 
    def end_date(self, end_date):
        if isinstance(end_date, str) and len(end_date) >= 7:
            self._end_date = end_date
        # else:
        #     raise Exception 
            
class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        # type(self).all.append(self)

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
        if not park.visitors():
            return 0
        return len([trip for trip in self.trips() if trip.national_park == park])