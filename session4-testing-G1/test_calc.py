from calc import Calculator

def test_add():
    # arrange
    calc = Calculator()

    # act
    result = calc.add(1, 2)

    # assert
    assert result == 3, f"Making sure that the result is correct add(1, 2) should be 3, not {result}"
    assert type(result) == int, "The result should be an integer"

    # assert calc.subtract(2, 1) == 1

def test_multiply():
    # arrange
    calc = Calculator()

    assert calc.multiply(3, 3) == 9

