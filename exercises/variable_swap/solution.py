from typing import Any

SUBMIT = True


def variable_swap(a: Any, b: Any) -> tuple[Any, Any]:
    a ,b = b, a
    return a, b


def test() -> None:
    """Simple self-test for Variable Swap."""
    cases = [(5, 10, (10, 5)), ("apple", "banana", ("banana", "apple"))]
    for a, b, expected in cases:
        try:
            res = variable_swap(a, b)
            assert res == expected, (
                f"Failed for a={a}, b={b}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
