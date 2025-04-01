import pytest
from triangle import classify_triangle

@pytest.mark.parametrize('a,b,c,expected',[
    (3,3,3,"equilateral"),
])
def test_triangle(a,b,c,expected):
    res = classify_triangle(a,b,c)
    assert res == expected


@pytest.mark.parametrize("a, b, c, expected", [
    (0, 0, 0, "invalid"),
    (1, 1, 1, "equilateral"),
    (2, 2, 3, "isosceles"),
    (3, 4, 5, "orthogonal"),
    (2, 3, 4, "other")
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected