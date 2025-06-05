### Testing code for Task1 ####
import pytest

from task1.Solution1 import TTTComputer, BoardIsFullException


@pytest.fixture
def game():
    return TTTComputer ()


def test_ranges(game):
    # looping here, because the result
    # obtained is random
    for x in range (10000):
        x, y = game.calculateNextMove ()
        assert x >= 0
        assert x < 3
        assert y >= 0
        assert y < 3


def test_overlapping(game):
    game.place_on (1, 1)
    game.place_on (2, 2)
    game.place_on (0, 1)
    game.place_on (2, 1)
    game.place_on (1, 2)
    for x in range (10000):
        assert (game.calculateNextMove () != (1, 1))
        assert (game.calculateNextMove () != (2, 2))
        assert (game.calculateNextMove () != (0, 1))
        assert (game.calculateNextMove () != (2, 1))
        assert (game.calculateNextMove () != (1, 2))


def test_no_more_move(game):
    for x in range (3):
        for y in range (3):
            game.place_on (x, y)
    with pytest.raises (BoardIsFullException):
        game.calculateNextMove ()