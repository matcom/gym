SUBMIT = True


def fibonacci(n: int) -> int:
    arr = [0, 1]
    if(n < 0):
        return 0
    elif(n < 2):
        return arr[n]
    for i in range(n - 1):
        arr[i % 2] = sum(arr)
    return arr[n % 2]


def test() -> None:
    """Simple self-test for Fibonacci."""
    cases = {0: 0, 1: 1, 5: 5, 10: 55}
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
