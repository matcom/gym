SUBMIT = True


def list_average(_numbers: list[float]) -> float:
    """Returns the mean of a numeric list."""
    
    if not _numbers:
        return 0
    s = sum(_numbers)
    l = len(_numbers)
    return s / l


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
