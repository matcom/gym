SUBMIT = True

def recursive_min_max(
    lst: list[int], low: int = 0, high: int | None = None
) -> tuple[int, int]:
    """Recursive Min/Max"""
    if high == None:
        high = len(lst)
    
    if low == high-1:
        min_value = lst[low]
        max_value = min_value
        return min_value, max_value
    
    mid = (low + high) // 2
    min_value = min(recursive_min_max(lst, low, mid)[0], recursive_min_max(lst, mid, high)[0])
    max_value = max(recursive_min_max(lst, low, mid)[1], recursive_min_max(lst, mid, high)[1])
    
    return min_value, max_value


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
