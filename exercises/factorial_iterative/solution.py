SUBMIT = True


def factorial_iterative(_n: int) -> int:
    # noqa: ARG001
    """Calculates n! using a loop."""
    f = 1
    while _n > 0:
        f *= _n
        _n -= 1
    return f

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
