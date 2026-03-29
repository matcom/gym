SUBMIT = True


def prefix_sums(_numbers: list[int]) -> list[int]:
    """Returns the cumulative sums of a list.

    Example usage:
    >>> prefix_sums([1, 2, 3])
    [1, 3, 6]
    >>> prefix_sums([10, -10, 5])
    [10, 0, 5]
    """
    arr = _numbers[:]
    n = len(arr)
    for i in range(1, n):
        arr[i] += arr[i - 1]
    return arr


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
