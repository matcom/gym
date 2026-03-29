SUBMIT = True


def fibonacci(n: int) -> int:
    sum1 = 0
    sum2 = 1
    solution = 1
    if n == 0 or n == 1:
        return n
    else:
        while solution != n:
            sum1 ,sum2 = sum2 , sum1 + sum2
            solution+=1
        
        return sum2 
 
    


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
