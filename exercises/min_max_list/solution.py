SUBMIT = True


def min_max_list(_items: list[int]) -> tuple[int, int] | None:
    if _items == []:
        return None
    max = _items[0]
    min = max
    for i in _items:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)


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
