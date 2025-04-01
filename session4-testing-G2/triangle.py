import math


def classify_triangle(a, b, c):
    # TODO: To be implemented...
    # Should return
    #   "equilateral",
    #   "isosceles",
    #   "orthogonal",
    #   "other" or
    #   "invalid"

    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return "orthogonal"
    if a == b == c:
        return "equilateral"
    if a == b or b == c or a == c:
        return "isosceles"
    if a <= 0 or b <= 0 or c <= 0:
        return "invalid"

    return "other"

    # l2 = [a, b, c]
    # if any(x <= 0 for x in l2):
    #     return "invalid"
    #
    # if a == b == c:
    #     return "equilateral"
    #
    # l1 = [a, b, c]
    # if len(set(l1)) == 2:
    #     return "isosceles"
    #
    # l1_sorted = sorted(l1, reverse=True)
    # if l1_sorted[0] == math.sqrt(l1_sorted[1]^2 + l1_sorted[2]^2):
    #     return "orthogonal"
    #
    # return "other"
