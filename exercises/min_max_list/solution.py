SUBMIT = True


def min_max_list(_items: list[int]) -> tuple[int, int] | None:
    """Find both min and max values in a list by iterating once."""
    
    if not _items:
        return None
    
    menor = _items[0]
    mayor = menor
    
    for i in range(1, len(_items)):
        if _items[i] < menor :
            menor = _items[i]
        if _items[i] > mayor:
            mayor = _items[i]
    
    return (menor, mayor)


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
