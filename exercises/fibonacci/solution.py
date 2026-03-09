SUBMIT = True


def fibonacci(n: int) -> int:
    """Calculates the n-th Fibonacci number.

    Example usage:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    """
        if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1): a, b = b, a + b
    return b
