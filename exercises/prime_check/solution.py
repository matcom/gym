SUBMIT = True


def prime_check(_n: int) -> bool:
    # noqa: ARG001
    """Checks if a number is prime"""
    if _n == 0 or _n == 1:
        return False
    raiz = _n**(1/2)
    
    i = 2
    while i <= raiz:
        if _n%i == 0:
            return False
        i += 1
    return True


def test() -> None:
    """Simple self-test for Primality Test."""
    cases = {2: True, 4: False, 17: True, 1: False, 0: False, 97: True}
    for n, expected in cases.items():
        try:
            res = prime_check(n)
            assert res == expected, f"Failed for n={n}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
