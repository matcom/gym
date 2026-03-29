SUBMIT = True


def factorial_iterative(_n: int) -> int:
    solution = 1
    for i in range(1,_n+1):
        solution*= i
    return solution

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
