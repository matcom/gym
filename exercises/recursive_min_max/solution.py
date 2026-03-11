SUBMIT = True


def recursive_min_max(
    lst: list[int], low: int = 0, high: int | None = None
) -> tuple[int, int]:
    if(high is None):
        high = len(lst) - 1

    if(low == high):
        return lst[low], lst[low]
    
    mid = (low + high) // 2
    _min0, _max0 = recursive_min_max(lst, low, mid)
    _min1, _max1 = recursive_min_max(lst, mid + 1, high)

    return min(_min0, _min1), max(_max0, _max1)
    


def test() -> None:
    """Simple self-test for Recursive Min/Max."""
    assert recursive_min_max([3, 1, 4, 1, 5, 9]) == (1, 9), (
        f"Expected (1, 9), got {recursive_min_max([3, 1, 4, 1, 5, 9])}"
    )
    assert recursive_min_max([42]) == (42, 42), (
        f"Expected (42, 42), got {recursive_min_max([42])}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
