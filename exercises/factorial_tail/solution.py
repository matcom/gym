SUBMIT = True


def factorial_tail(n: int, acc: int = 1) -> int:
    if n == 0:
        return 1
    else: return(n * (factorial_tail(n-1)))


def test() -> None:
    """Simple self-test for Factorial Tail."""
    assert factorial_tail(5) == 120, f"Expected 120, got {factorial_tail(5)}"
    assert factorial_tail(0) == 1, f"Expected 1, got {factorial_tail(0)}"
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
