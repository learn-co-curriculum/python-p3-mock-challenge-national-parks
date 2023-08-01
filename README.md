# Mock Code Challenge - National Parks (Object Relationships)

For this assignment, we'll be working with a national park planner-style domain.

We have three models: `NationalPark`, `Visitor`, and `Trip`.

For our purposes, a `NationalPark` has many `Trip`s, a `Visitor` has many
`Trip`s, and a `Trip` belongs to a `Visitor` and to a `NationalPark`.

`NationalPark` - `Visitor` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory. Then run `pipenv shell` to jump into the shell.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Visitor

- `Visitor __init__(self, name)`
  - Visitor should be initialized with a name
- `Visitor property name`
  - Return name
  - Names must be of type `str`
  - Names must be between 1 and 15 characters, inclusive

#### NationalPark

- `NationalPark __init__(self, name)`
  - national_parks should be initialized with a name, as a string
- `NationalPark property name`
  - Returns the NationalPark's name
  - Should not be able to change after the NationalPark is created
  - _hint: hasattr()_

#### Trip

- `Trip __init__(self, visitor, national_park, start_date, end_date)`
  - Trips should be initialized with a visitor, national_park, start_date(str), end_date(str)

### Object Relationship Methods and Properties

#### Trip

- `Trip property visitor`
  - Returns the visitor object for that trip
  - Must be of type `Visitor`
- `Trip property national_park`
  - Returns the NationalPark object for that trip
  - Must be of type `NationalPark`

#### Visitors

- `Visitor trips()`
  - Returns a list of all trips for that visitor
  - The list of trips must contain objects of type `Trip`
- `Visitor national_parks()`
  - Returns a **unique** list of all parks who that visitor has visited.
  - The list of national parks must contain objects of type `NationalPark` 

#### NationalPark

- `NationalPark trips()`
  - Returns a list of all trips planned for this national park
  - The list of trips must contain objects of type `Trip`
- `NationalPark visitors()`
  - Returns a **unique** list of all visitors a national park has received
  - The list of visitors must contain objects of type `Visitor`

### Aggregate and Association Methods

#### National Park

- `NationalPark total_visits()`
  - Returns the total number of times that park has been visited
- `NationalPark best_visitor()`
  - Returns the Visitor who has visited the park the most

#### Visitor

- `Visitor total_visits_at_park(self, park)`
  - Returns the total number of times a visitor visited the park passed in as argument
  - Returns 0 if the visitor has never visited the park

### Bonus: Aggregate and Association Method

- `NationalPark classmethod most_visited(cls, game)`
  - Returns the `NationalPark` instance with the most visits.
  - Returns `None` if there are no visits.
  - _hint: will need a way to remember all `NationalPark` objects_
  - _hint: do you have a method to get the total visits for a
    particular `NationalPark` object?_
  - Uncomment lines in the national_park_test file
### Bonus: For any invalid inputs raise an `Exception`.

Uncomment the following lines in the test files:

#### national_park_test.py

- lines 20-21 and 29-30

#### visitor_test.py

- lines 20-21 and 29-30