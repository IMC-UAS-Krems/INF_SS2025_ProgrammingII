from naivetesting import check_allowed

def test_naivetesting_tooYoungShouldReturnSorry():
    # act
    response = check_allowed(6)
    # assert
    assert response == "sorry", "The test was okay with age 6"
