SUBMIT = True


def fast_exponentiation(a: int, n: int) -> int:
    if n == 0 :
        return 1
    else :
        return a * fast_exponentiation(a,n-1)


def test() -> None:
    """Simple self-test for Fast Exponentiation."""
    assert fast_exponentiation(2, 10) == 1024, (
        f"Expected 1024, got {fast_exponentiation(2, 10)}"
    )
    assert fast_exponentiation(5, 3) == 125, (
        f"Expected 125, got {fast_exponentiation(5, 3)}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
