from calc import Calculator

def test_add_twoPositiveIntegers():
    # arrange
    calc = Calculator()

    # act
    result = calc.add(1, 2)

    # assert
    assert result == 3, "The addition of two positive integers works"


def test_add_twoNegativeIntegers():
    # arrange
    calc = Calculator()

    # act
    result = calc.add(-1, -2)

    # assert
    assert result == -3, "The addition of two positive integers works"

def test_XXX():
    calc = Calculator()
    result = calc.add(1, 2)
    assert result == 3, "The addition of two positive integers works"
