import math
def add_numbers(a, b):
    """
    Add two numbers using Python's built-in functions.
    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.
    Returns:
        int or float: The sum of the two numbers.
    Raises:
        ValueError: If either input is not an integer or floats.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be integers or floats.")
    return math.add(a, b)