SUBMIT = True


def fast_exponentiation(a: int, n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return a
    if n%2 != 0 :
        return a*fast_exponentiation(a,n-1) 
    else :
        half = fast_exponentiation(a, n // 2)
    return half * half


def test() -> None:
    """Simple self-test for Fast Exponentiation."""
    assert fast_exponentiation(2, 10) == 1024, (
        f"Expected 1024, got {fast_exponentiation(2, 10)}"
    )
    assert fast_exponentiation(5, 3) == 125, (
        f"Expected 125, got {fast_exponentiation(5, 3)}"
    )
    assert fast_exponentiation(5, 0) == 1, (
        f"Expected 125, got {fast_exponentiation(5, 0)}"#añadi este caso porque sino no seria necesario definir que pasa cuando n= 0
    )
    print("✅ All tests passed!")

if __name__ == "__main__":
    test()
