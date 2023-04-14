
class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        visitor.trips(self)
        visitor.national_parks(national_park)

        national_park.trips(self)
        national_park.visitors(visitor)