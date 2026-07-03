SUBMIT = True


def factorial_iterative(_n: int) -> int:
    # noqa: ARG001
    """Calculates n! using a loop.

    Example usage:
    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(5)
    120
    """
    if _n==0:
        return 1
    fact=1
    for i in range(1,_n+1):
        fact*=i
    return fact


def test() -> None:
    """Simple self-test for Iterative Factorial."""
    cases = {0: 1, 1: 1, 5: 120, 10: 3628800}
    for n, expected in cases.items():
        try:
            res = factorial_iterative(n)
            assert res == expected, f"Failed for n={n}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
