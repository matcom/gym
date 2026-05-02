SUBMIT = True


def fibonacci_tail(n: int, a: int = 0, b: int = 1) -> int:
    """Tail Recursive Fibonacci"""
    if n == 0:
        return a
    elif n == 1:
        return b
    
    c = a+b
    return fibonacci_tail(n-1, b, c)


def test() -> None:
    """Simple self-test for Fibonacci Tail."""
    assert fibonacci_tail(0) == 0, f"Expected 0, got {fibonacci_tail(0)}"
    assert fibonacci_tail(5) == 5, f"Expected 5, got {fibonacci_tail(5)}"
    assert fibonacci_tail(10) == 55, f"Expected 55, got {fibonacci_tail(10)}"
    assert fibonacci_tail(50) == 12586269025, f"Expected 12586269025, got {fibonacci_tail(50)}"
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
