SUBMIT = True


def min_max_list(_items: list[int]) -> tuple[int, int] | None:
    """Find both min and max values in a list by iterating once.

    Example usage:
    >>> min_max_list([3, 1, 4, 1, 5, 9, 2, 6, 5])
    (1, 9)
    >>> min_max_list([10])
    (10, 10)
    >>> min_max_list([])
    None
    """
    n = len(_items)
    if(n <= 0): return None
    _min, _max = _items[0], _items[0] 
    for i in range(1, n):
        _min = min(_items[i], _min)
        _max = max(_items[i], _max)
    return (_min, _max)


def test() -> None:
    """Simple self-test for Min/Max List."""
    cases = [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], (1, 9)),
        ([10], (10, 10)),
        ([], None),
        ([-1, -5, 0, 10], (-5, 10)),
    ]
    for items, expected in cases:
        try:
            res = min_max_list(items)
            assert res == expected, (
                f"Failed for {items}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
