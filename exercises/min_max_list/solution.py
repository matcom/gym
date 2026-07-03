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
    # El mayor entero que cabe en una "palabra" de memoria (64 bits)
    a = float('inf')
    b = float('-inf')
    if  not _items:
        return None
    for i in _items:
        if i > b:
            b =i
        if i < a:
            a=i  
    return (a,b)


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
