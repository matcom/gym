SUBMIT = True


def prefix_sums(_numbers: list[int]) -> list[int]:
    """Returns the cumulative sums of a list"""
    numbers_sum = []
    for i in range(len(_numbers)):
        count = _numbers[i]
        for j in range(i):
            count += _numbers[j]
        numbers_sum.append(count)
    return numbers_sum


def test() -> None:
    """Simple self-test for Cumulative Sums."""
    cases = [([1, 2, 3], [1, 3, 6]), ([10, -10, 5], [10, 0, 5])]
    for nums, expected in cases:
        try:
            res = prefix_sums(nums)
            assert res == expected, f"Failed for {nums}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
