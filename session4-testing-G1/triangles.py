def def_triangle(a, b, c):
    """
    Function to check if three sides can form a triangle.
    """
    if a == b and b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
        return "Orthogolnal triangle"
    else:
        return "Other valid triangle triangle"
