SUBMIT = True


def list_average(_numbers: list[float]) -> float:
    if _numbers == []:
        return 0.0
    solution = 0
    for i in _numbers:
        solution += i 
    return solution/len(_numbers) 


def test() -> None:
    """Simple self-test for Computing Average."""
    cases = [([1, 2, 3, 4, 5], 3.0), ([10, 20, 30], 20.0), ([5], 5.0)]
    for nums, expected in cases:
        try:
            res = list_average([float(x) for x in nums])
            assert abs(res - expected) < 1e-9, (
                f"Failed for {nums}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
