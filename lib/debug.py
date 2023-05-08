#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    visitor1 = Visitor("Bob")
    visitor2 = Visitor("Queena")
    visitor3 = Visitor("Jolie")
    
    np1 = NationalPark("Central Park")
    np2 = NationalPark("Grand Canyon")
    
    trip1 = Trip(visitor1, np1, "April 2nd", "April 4th")
    trip2 = Trip(visitor1, np2, "May 6th", "May 8th")
    trip3 = Trip(visitor3, np2, "January 12th", "January 20th")
    trip4 = Trip(visitor2, np1, "December 24th", "December 29th")
    
    ipdb.set_trace()
