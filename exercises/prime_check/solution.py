import math
SUBMIT = True

#optimizado , se parece cantidad a una induccion fuerte jjj
def prime_check(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:
            return False
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
