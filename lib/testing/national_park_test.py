from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip
import pytest

class TestNationalParks:
    '''NationalPark in national_park.py'''

    def test_has_name(self):
        '''NationalPark is initialized with a name'''
        np = NationalPark("Flatirons")
        assert (np.name == "Flatirons")

    def test_name_is_string(self):
        '''NationalPark is initialized with a name of type str'''
        np = NationalPark("Wild West")
        assert (isinstance(np.name, str))
        np_2 = NationalPark(2)
        assert (not hasattr(np_2, "_name"))

    def test_name_setter(self):
        '''Cannot change the name of the NationalPark'''
        np = NationalPark("under the sea")
        np.name = "over the sea"
        assert (np.name == "under the sea")

    def test_has_many__trips(self):
        '''NationalPark has many Trips.'''
        p1 = NationalPark("Yosemmette")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor('Steve')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th","May 27th")
        t_3 = Trip(vis, p2, "January 5th","January 20th")

        assert (len(p1.trips()) == 2)
        assert (t_1 in p1.orders())
        assert (t_2 in p1.orders())
        assert (not t_3 in p1.orders())

    def test_trips_of_type_trips(self):
        '''National Park trips are of type '''
        vis = Visitor("Phil")
        p1 = NationalPark('Yellow Stone')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th","May 27th")

        assert (isinstance(p1.trips()[0], Trip))
        assert (isinstance(p1.trips()[1], Trip))

    def test_has_many_visitors(self):
        '''National Parks has many visitors.'''
        vis = Visitor("Tammothy")
        vis2 = Visitor('Bryce')

        p1 = NationalPark('Alaska Wilds')
        
        t_1 = Trip(vis, p1, 2)
        t_2 = Trip(vis2, p1, 5)

        assert (p1 in vis.nationalparks())
        assert (p1 in vis2.nationalparks())

    def test_has_unique_visitors(self):
        '''NationalParks has unique list of all the visitors that have visited.'''

        p1 = NationalPark("Yosemmette")
        vis = Visitor('Steeve')
        vis2 = Visitor('Wolfe')

        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th","May 27th")
        t_3 = Trip(vis2, p1, "January 5th","January 20th")

        assert (len(set(p1.visitors())) == len(p1.visitors()))
        assert (len(p1.visitors()) == 2)

    def test_total_visits(self):
        '''Correct total visits'''
        p1 = NationalPark("Yosemmette")
        vis = Visitor('Sheryl')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "June 20th", "July 4th")
        t_3 = Trip(vis, p1, "January 5th","January 20th")
        assert (len(p1.total_visits()) == 3)
    
    def test_best_visitor(self):
        '''Get the visitor that visited the park the most'''
        p1 = NationalPark("Yosemmette")
        vis = Visitor('Tom')
        vis2 = Visitor('Mark')
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_3 = Trip(vis, p1, "January 5th","January 20th")
        t_3 = Trip(vis2, p1, "January 5th","January 20th")
        assert(p1.best_visitor().name == "Tom")
