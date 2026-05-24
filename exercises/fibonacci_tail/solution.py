SUBMIT = True


def fibonacci_tail(n: int, a: int = 0, b: int = 1) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    else: return fibonacci_tail(n-1) + fibonacci_tail(n-2)
    


def test() -> None:
    """Simple self-test for Fibonacci Tail."""
    assert fibonacci_tail(0) == 0, f"Expected 0, got {fibonacci_tail(0)}"
    assert fibonacci_tail(5) == 5, f"Expected 5, got {fibonacci_tail(5)}"
    assert fibonacci_tail(10) == 55, f"Expected 55, got {fibonacci_tail(10)}"
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
