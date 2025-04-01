import pytest
import random_passoword_generator

@pytest.mark.parametrize('inp,exp',[
    ('aaa',True),
    ('123!!',True),
    ('abcde',False),
    ('abc cba',False),
]
)
def test_is_repeating(inp,exp):
    assert random_passoword_generator._is_repeating(inp) == exp
