# string_utils.py

def reverse_string(s):
    """Reverses a given string."""
    if not isinstance(s, str):
        # Good unit tests should handle unexpected inputs
        raise TypeError("Input must be a string")
    return s[::-1]

def is_palindrome(s):
    """Checks if a string is a palindrome (reads the same forwards and backwards)."""
    s = s.lower().replace(" ", "") # Normalize the string
    return s == s[::-1]