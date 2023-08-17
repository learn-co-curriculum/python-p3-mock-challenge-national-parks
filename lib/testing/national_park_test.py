import pytest

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip


class TestNationalParks:
    """NationalPark in many_to_many.py"""

    def test_has_name(self):
        """NationalPark is initialized with a name"""
        np = NationalPark("Flatirons")
        assert np.name == "Flatirons"

    def test_name_is_valid_string(self):
        """NationalPark is initialized with a name of type str longer than 3 chars"""
        np = NationalPark("Wild West")
        assert isinstance(np.name, str)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     NationalPark(2)
        
        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     NationalPark("me")

    def test_name_setter(self):
        """cannot change the name of the national_park"""
        np = NationalPark("under the sea")

        # comment out the next two lines if using Exceptions
        np.name = "over the sea"
        assert np.name == "under the sea"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     np.name = "over the sea"

    def test_has_many_trips(self):
        """national_park has many trips"""
        p_1 = NationalPark("Yosemite")
        p_2 = NationalPark("Rocky Mountain")
        vis_1 = Visitor("Steve")
        t_1 = Trip(vis_1, p_1, "May 5th", "May 9th")
        t_2 = Trip(vis_1, p_1, "May 20th", "May 27th")
        t_3 = Trip(vis_1, p_2, "January 5th", "January 20th")

        assert len(p_1.trips()) == 2
        assert len(p_2.trips()) == 1
        assert t_1 in p_1.trips()
        assert t_2 in p_1.trips()
        assert t_3 not in p_1.trips()
        assert t_3 in p_2.trips()

    def test_trips_of_type_trip(self):
        """national_park trips are of type Trip"""
        vis_1 = Visitor("Phil")
        p_1 = NationalPark("Yellow Stone")
        Trip(vis_1, p_1, "May 5th", "May 9th")
        Trip(vis_1, p_1, "May 20th", "May 27th")

        assert isinstance(p_1.trips()[0], Trip)
        assert isinstance(p_1.trips()[1], Trip)

    def test_has_many_visitors(self):
        """national_park has many visitors."""
        vis_1 = Visitor("Tammothy")
        vis_2 = Visitor("Bryce")
        vis_3 = Visitor("Wolfe")
        p_1 = NationalPark("Alaska Wilds")

        Trip(vis_1, p_1, "February 2nd", "February 3rd")
        Trip(vis_2, p_1, "February 5th", "February 9th")

        assert vis_1 in p_1.visitors()
        assert vis_2 in p_1.visitors()
        assert vis_3 not in p_1.visitors()

    def test_has_unique_visitors(self):
        """national_park has unique list of all the visitors that have visited."""

        p_1 = NationalPark("Yosemite")
        vis_1 = Visitor("Steeve")
        vis_2 = Visitor("Wolfe")

        Trip(vis_1, p_1, "May 5th", "May 9th")
        Trip(vis_1, p_1, "May 20th", "May 27th")
        Trip(vis_2, p_1, "January 5th", "January 20th")

        assert len(set(p_1.visitors())) == len(p_1.visitors())
        assert len(p_1.visitors()) == 2

    def test_visitors_of_type_visitor(self):
        """national_park visitors are of type Visitor"""
        vis_1 = Visitor("Phil")
        vis_2 = Visitor("Wolfe")
        p_1 = NationalPark("Yellow Stone")
        Trip(vis_1, p_1, "May 5th", "May 9th")
        Trip(vis_2, p_1, "May 20th", "May 27th")

        assert isinstance(p_1.visitors()[0], Visitor)
        assert isinstance(p_1.visitors()[1], Visitor)

    def test_total_visits(self):
        """national_park tracks total visits"""
        p_1 = NationalPark("Yosemite")
        vis_1 = Visitor("Sheryl")
        Trip(vis_1, p_1, "May 5th", "May 9th")
        Trip(vis_1, p_1, "June 20th", "July 4th")
        Trip(vis_1, p_1, "January 5th", "January 20th")

        assert p_1.total_visits() == 3

    def test_best_visitor(self):
        """returns visitor that visited the park the most"""
        p_1 = NationalPark("Yosemite")
        vis_1 = Visitor("Tom")
        vis_2 = Visitor("Mark")
        Trip(vis_1, p_1, "May 5th", "May 9th")
        Trip(vis_1, p_1, "January 5th", "January 20th")
        Trip(vis_2, p_1, "January 5th", "January 20th")
        assert p_1.best_visitor().name == "Tom"


#     def test_most_visited(self):
#         """returns the most visited park"""
#         p_1 = NationalPark("Yosemite")
#         p_2 = NationalPark("Yellow Stone")
#         vis_1 = Visitor("Tom")
#         Trip(vis_1, p_1, "May 5th", "May 9th")
#         Trip(vis_1, p_1, "January 5th", "January 20th")
#         Trip(vis_1, p_2, "January 25th", "January 30th")
#         assert NationalPark.most_visited().name == "Yosemite"
