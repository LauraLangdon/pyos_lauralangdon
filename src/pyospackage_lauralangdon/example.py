"""
A module that adds numbers together or adds rainbows to text.
"""

def add_numbers(a, b):
    """
    Add two numbers together and return the result.

    This is an example function with a numpy style docstring.
    We recommend using this style for consistency and readability.

    Parameters
    ----------
    a : float
        The first number to add.
    b : float
        The second number to add.

    Returns
    -------
    float
        The sum of the two numbers.

    Examples
    --------
    >>> add_numbers(3, 5)
    8
    >>> add_numbers(-2, 7)
    5

    """
    return a + b

def add_rainbows(some_text):
    """
    A function that adds rainbows to text

    Parameters
    ----------
    some_text: string
        Text to get rainbows added to it.

    
    Returns
    -------
    string
        The text with a rainbow added to the beginning and end.

    Example
    --------
    >>> add_rainbows("Everything is better with rainbows")
    🌈 Everything is better with rainbows 🌈
    """

    return ("🌈 " + some_text + " 🌈")

    