import pytest
from some_maths import cube

###############################################################################
# V1: Introducing the parametrize fixture
###############################################################################
@pytest.mark.parametrize("test_input,expected", [(3, 27), (2, 8), (10, 1000)])
def test_cube_fn_is_correct_v1(test_input, expected):
    """
    Test that the `cube()` returns the correct result!
    """

    # Run the function
    result = cube(test_input)
    
    # Verify that the result, is what you expected
    assert result == expected


###############################################################################
# V2: Adding in 'xfail' - marking that you eXpect the test to fail
###############################################################################
@pytest.mark.parametrize("test_input,expected", [(3, 27), (2, 8), pytest.param(10, 1001, marks=pytest.mark.xfail)])
def test_cube_fn_is_correct_v2(test_input, expected):
    """
    Test that the `cube()` returns the correct result!
    """

    # Run the function
    result = cube(test_input)

    # Verify that the result, is what you expected
    assert result == expected


###############################################################################
# V3: Adding IDs to your tests for readability
###############################################################################
test_data = [
    (3, 27),
    (-3, -27),
]

@pytest.mark.parametrize("test_input,expected", test_data, ids=["positive_cube", "negative_cube"])
def test_cube_fn_is_correct_v3(test_input, expected):
    """
    Test that the `cube()` returns the correct result!
    """

    # Run the function
    result = cube(test_input)

    # Verify that the result, is what you expected
    assert result == expected