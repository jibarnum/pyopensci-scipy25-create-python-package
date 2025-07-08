"""
A module that does higher-level mathematics operations.
"""

def exponential(a: float, b: float) -> float:
    """
    Create an exponential of two numbers together and return the result.

    Parameters
    ----------
    a : float
        The constant.
    b : float
        The variable.

    Returns
    -------
    float
        The exponential of the two numbers (the constant and the variable).

    Examples
    --------
    >>> exponential(3, 5)
    243
    >>> exponential(-2, 2)
    -4

    """
    return a ** b