from some_maths import cube


def test_cube_fn_is_correct():
    """
    Test that the `cube()` returns the correct result!
    """
    
    # Define the inputs
    input_value = 3
    
    # Define what you expect to happen
    expected_result = 27
    
    # Run the function
    result = cube(input_value)
    
    # Verify that the result, is what you expected
    assert result == expected_result
