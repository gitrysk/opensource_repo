
def num_power(num1, exponent):
    """
    Raises a number to a given exponent.

    Args:
        num1 (float): The base number to be raised to the power.
        exponent (float): The exponent to which the base number is raised.

    Returns:
        float: The result of raising the base number to the given exponent.

    Examples:
        >>> num_power(2, 3)
        8.0
        >>> num_power(4.5, 2)
        20.25
        >>> num_power(3, -1)
        0.3333333333333333
    """
    return num1**exponent
