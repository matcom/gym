SUBMIT = True


def fibonacci(n: int) -> int:
    """Calculates the n-th Fibonacci number."""
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def test() -> None:
    """Simple self-test for Fibonacci."""
    cases = {0: 0, 1: 1, 5: 5, 10: 55, 30: 832040}
    for n, expected in cases.items():
        try:
            res = fibonacci(n)
            assert res == expected, f"Failed for n={n}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
