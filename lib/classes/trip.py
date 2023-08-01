class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self._visitor = visitor
        self._national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def name(self, visitor):
        if isinstance(visitor, Visitor):
            raise Exception
        else:
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if isinstance(national_park, NationalPark):
            raise Exception
        else:
            self._national_park = national_park


from classes.visitor import Visitor
from classes.national_park import NationalPark