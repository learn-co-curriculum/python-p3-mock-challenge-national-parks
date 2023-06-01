class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self,'name') and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception 

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips 
        pass
        
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor not in self._visitors and isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return self._visitors 
        pass
    
    def total_visits(self):
        # trips give you amount of times park is visited
        return len(self._trips)
        pass
    
    def best_visitor(self):
        # micheals code
        # return max(set(self._visitors), key=self._visitors.count)
        visitor = None
        visit_num = 0 
        for v in self._visitors:
            visits =  self._visitors.count(v)
            if visits > visit_num:
                visitor = v
                visit_num = visits
        return visitor 
    # rabs main from the for loop 
        pass