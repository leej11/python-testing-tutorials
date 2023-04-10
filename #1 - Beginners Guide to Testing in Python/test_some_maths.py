from some_maths import cube


def test_cube_fn_is_correct():
    """
    Test that the `cube()` function returns the correct mathematical result.
    """

    # Define your inputs
    input_value = 2

    # Define your expected result
    expected_result = 8

    # Run the function that you are testing
    result = cube(input_value)

    # Verify that the result, is what you expected
    assert result == expected_result