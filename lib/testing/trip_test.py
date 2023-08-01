import pytest

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

class TestTrip:
    '''Trip in trip.py'''

    def test_has_start_date(self):
        '''Trip is initialized with a start_date'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (trip.start_date == "May 5th")

    def test_start_date_is_string(self):
        '''Trip is initialized with a start_date of type str'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (isinstance(trip.start_date, str))
    
    def test_has_end_date(self):
        '''Trip is initialized with a end_date'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (trip.end_date == "May 9th")
        
    def test_end_date_is_string(self):
        '''Trip is initialized with a end_date of type str'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (isinstance(trip.end_date, str))
    
    def test_has_visitor(self):
        '''Trip is initialized with a visitor'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (trip.visitor == matteo)
    
    def test_visitor_of_type_visitor(self):
        '''Trip visitor is of type Visitor'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (isinstance(trip.visitor, Visitor))
    
    def test_has_national_park(self):
        '''Trip is initialized with a national_park'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (trip.national_park == yosemite)
        
    def test_national_park_of_type_national_park(self):
        '''Trip national_park is of type NationalPark'''
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        trip = Trip(matteo, yosemite, "May 5th", "May 9th")
        assert (isinstance(trip.national_park, NationalPark))
    
    def test_get_all_trips(self):
        '''Test Trip class all attribute'''
        Trip.all = []
        yosemite = NationalPark("Yosemite")
        matteo = Visitor("Matteo")
        john = Visitor("John")
        Trip(matteo, yosemite, "May 5th", "May 9th")
        Trip(matteo, yosemite, "May 20th","May 27th")
        Trip(john, yosemite, "January 5th","January 20th")
        assert (len(Trip.all) == 3)