"""This package is a collection of several Abstract Datatypes (ADTs).

It contains the Person Module and Event Module, for representing
available events and people to be place on those event rosters.
"""

from .event import Event
from .person import Person

__all__ = ["Event", "Person"]
