def distance_between_points(a, b):
    return round(((a.x-b.x)**2+(a.y-b.y)**2)**0.5,6)
    # your code here


    """This series of katas will introduce you to basics of doing geometry with computers.

Point objects have x and y attributes (X and Y in C#) attributes.

Write a function calculating distance between Point a and Point b.

Tests round answers to 6 decimal places."""

from math import hypot

def distance_between_points(a, b):
    return hypot(a.x - b.x, a.y - b.y)
