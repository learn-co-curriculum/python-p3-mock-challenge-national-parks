import pytest

from classes.many_to_many import NationalPark
from classes.many_to_many import Visitor
from classes.many_to_many import Trip


class TestVisitor:
    """Visitor in many_to_many.py"""

    def test_has_name(self):
        """Visitor is initialized with a name"""
        visitor = Visitor("John")
        assert visitor.name == "John"

    def test_name_is_mutable_string(self):
        """Visitor is initialized with a name of type str"""
        visitor = Visitor("Bob")
        assert isinstance(visitor.name, str)

        # does not mutate name if value is not a string
        # comment out the next two lines if using Exceptions
        visitor.name = 2
        assert visitor.name == "Bob"

        # does mutate name if value is a valid string
        visitor.name = "Steve"
        assert visitor.name == "Steve"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Visitor(2)

    def test_name_has_valid_length(self):
        """can change the visitor's name if between 1 and 15 characters long"""
        vis = Visitor("Poppy")
        assert vis.name == "Poppy"

        # comment out the next two lines if using Exceptions
        vis.name = "TooLongTobeValid"
        assert vis.name == "Poppy"

        # comment out the next two lines if using Exceptions
        vis.name = ""
        assert vis.name == "Poppy"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Visitor("")

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Visitor("TooLongTobeValid")

    def test_has_many_trips(self):
        """visitor has many Trips"""
        p1 = NationalPark("Yosemite")
        vis = Visitor("Bill")
        vis2 = Visitor("Steve")
        t_1 = Trip(vis, p1, "May 5th", "May 9th")
        t_2 = Trip(vis, p1, "May 20th", "May 27th")
        t_3 = Trip(vis2, p1, "January 5th", "January 20th")

        assert len(vis.trips()) == 2
        assert t_1 in vis.trips()
        assert t_2 in vis.trips()
        assert t_3 not in vis.trips()

    def test_trips_of_type_trips(self):
        """visitor trips are of type Trip"""
        vis = Visitor("Phil")
        p1 = NationalPark("Yellow Stone")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")

        assert isinstance(vis.trips()[0], Trip)
        assert isinstance(vis.trips()[1], Trip)

    def test_has_many_parks(self):
        """visitor has many parks."""
        vis_1 = Visitor("Flat White")
        vis_2 = Visitor("Steve")
        p1 = NationalPark("Alaska Wilds")
        p2 = NationalPark("Bryce Canyon")
        Trip(vis_1, p1, "May 5th", "May 9th")
        Trip(vis_1, p2, "May 20th", "May 27th")
        Trip(vis_2, p2, "August 20th", "August 27th")

        assert len(vis_1.national_parks()) == 2
        assert len(vis_2.national_parks()) == 1
        assert p1 in vis_1.national_parks()
        assert p2 in vis_1.national_parks()
        assert p1 not in vis_2.national_parks()
        assert p2 in vis_2.national_parks()

    def test_has_unique_parks(self):
        """visitor has unique list of all the parks they have visited."""
        p1 = NationalPark("Yosemite")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor("Steeve")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p1, "May 20th", "May 27th")
        Trip(vis, p2, "January 5th", "January 20th")

        assert len(set(vis.national_parks())) == len(vis.national_parks())
        assert len(vis.national_parks()) == 2

    def test_parks_of_type_park(self):
        """visitor national_parks are of type NationalPark"""
        p1 = NationalPark("Yosemite")
        p2 = NationalPark("Rocky Mountain")
        vis = Visitor("Steeeve")
        Trip(vis, p1, "May 5th", "May 9th")
        Trip(vis, p2, "January 5th", "January 20th")

        assert isinstance(vis.national_parks()[0], NationalPark)
        assert isinstance(vis.national_parks()[1], NationalPark)

    def total_visits_at_park(self):
        """returns the total number of times a visitor has visited a park."""
        vis = Visitor("Phil")
        yosemite = NationalPark("Yosemite")
        rocky_mountain = NationalPark("Rocky Mountain")
        Trip(vis, yosemite, "May 5th", "May 9th")
        Trip(vis, yosemite, "May 20th", "May 27th")
        Trip(vis, yosemite, "January 5th", "January 20th")
        Trip(vis, rocky_mountain, "January 5th", "January 20th")

        assert vis.total_visits_at_park(yosemite) == 3
        assert vis.total_visits_at_park(rocky_mountain) == 1
