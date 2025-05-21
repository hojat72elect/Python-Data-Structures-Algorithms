def factorial(n: int) -> int:
    """
    Returns the factorial of n.
    n must be a non-negative integer.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


