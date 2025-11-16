# test_calculator.py
# Pytest requires test functions to start with 'test_'

from calculator import add, subtract

def test_add_positive_numbers():
    """Test case 1: Checks addition of two positive integers."""
    # Arrange: Not strictly needed here, inputs are clear
    # Act: Call the function
    result = add(5, 8)
    # Assert: Check if the result matches the expectation
    assert result == 13

def test_subtract_negative_result():
    """Test case 2: Checks subtraction resulting in a negative number."""
    result = subtract(10, 25)
    assert result == -15

def test_add_with_zero():
    """Test case 3: Checks addition involving zero."""
    result = add(0, 7)
    assert result == 7