import pytest
from some_maths import cube

###############################################################################
# V1: Introducing the parametrize fixture
###############################################################################
@pytest.mark.parametrize("test_input,expected", [(2,8), (0,0), (-2, -8), (10, 1000)])
def test_cube_fn_is_correct_v1(test_input, expected):

    result = cube(test_input)
    assert result == expected



###############################################################################
# V2: Adding IDs to your tests for readability
###############################################################################
test_data = [
(2,8), (0,0), (-2, -7), (10,1000)
]


@pytest.mark.parametrize("test_input,expected", test_data, ids=['positive_integer', 'zero', 'negative_integer', 'large_integer'])
def test_cube_fn_is_correct_v2(test_input, expected):

    result = cube(test_input)
    assert result == expected