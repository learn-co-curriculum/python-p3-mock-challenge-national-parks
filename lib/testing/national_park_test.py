import pytest

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

class TestNationalParks:
    """NationalPark in national_park.py"""

    def test_has_name(self):
        """NationalPark is initialized with a name"""
        np = NationalPark("Flatirons")
        assert np.name == "Flatirons"

    def test_name_is_string(self):
        """NationalPark is initialized with a name of type str"""
        np = NationalPark("Wild West")
        assert isinstance(np.name, str)

        # with pytest.raises(Exception):
        #     NationalPark(2)

    def test_name_setter(self):
        """Cannot change the name of the NationalPark"""
        np = NationalPark("under the sea")

        # comment the next two lines if using Exceptions
        np.name = "over the sea"
        assert np.name == "under the sea"

        # with pytest.raises(Exception):
        #     np.name = "over the sea"

    def test_has_many__trips(self):
        """NationalPark has many Trips."""
        p1 = NationalPark("Yosemite")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor("Steve")
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th", "May 27th")
        t_3 = Trip(vis, p2, "January 5th", "January 20th")

        assert len(p1.trips()) == 2
        assert t_1 in p1.trips()
        assert t_2 in p1.trips()
        assert t_3 not in p1.trips()

    def test_trips_of_type_trips(self):
        """National Park trips are of type"""
        vis = Visitor("Phil")
        p1 = NationalPark("Yellow Stone")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")

        assert isinstance(p1.trips()[0], Trip)
        assert isinstance(p1.trips()[1], Trip)

    def test_has_many_visitors(self):
        """National Parks has many visitors."""
        vis = Visitor("Tammothy")
        vis2 = Visitor("Bryce")

        p1 = NationalPark("Alaska Wilds")

        Trip(vis, p1, "2/2", "2/3")
        Trip(vis2, p1, "2/5", "2/9")

        assert vis in p1.visitors()
        assert vis2 in p1.visitors()

    def test_has_unique_visitors(self):
        """NationalParks has unique list of all the visitors that have visited."""

        p1 = NationalPark("Yosemite")
        vis = Visitor("Steeve")
        vis2 = Visitor("Wolfe")

        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")
        Trip(vis2, p1, "January 5th", "January 20th")

        assert len(set(p1.visitors())) == len(p1.visitors())
        assert len(p1.visitors()) == 2

    def test_total_visits(self):
        """Correct total visits"""
        p1 = NationalPark("Yosemite")
        vis = Visitor("Sheryl")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "June 20th", "July 4th")
        Trip(vis, p1, "January 5th", "January 20th")
        assert p1.total_visits() == 3

    def test_best_visitor(self):
        """Get the visitor that visited the park the most"""
        p1 = NationalPark("Yosemite")
        vis = Visitor("Tom")
        vis2 = Visitor("Mark")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "January 5th", "January 20th")
        Trip(vis2, p1, "January 5th", "January 20th")
        assert p1.best_visitor().name == "Tom"

#     def test_most_visited(self):
#         """Get the most visited park"""
#         p1 = NationalPark("Yosemite")
#         p2 = NationalPark("Yellow Stone")
#         vis = Visitor("Tom")
#         Trip(vis, p1, "May 5th", "May 9th")
#         Trip(vis, p1, "January 5th", "January 20th")
#         Trip(vis, p2, "January 25th", "January 30th")
#         assert NationalPark.most_visited().name == "Yosemite"