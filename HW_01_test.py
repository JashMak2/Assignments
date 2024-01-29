import pytest
from HW_01 import classify_triangle

def test_scalene_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene Right Triangle"

def test_equilateral_triangle():
    assert classify_triangle(5, 5, 5) == "Equilateral Triangle"

def test_isosceles_triangle():
    assert classify_triangle(4, 4, 7) == "Isosceles"

def test_invalid_triangle():
    assert classify_triangle(3, 4, 3) == "Not a valid triangle"
