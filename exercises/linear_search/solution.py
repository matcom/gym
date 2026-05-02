SUBMIT = True


def linear_search(_items: list[int], _target: int) -> int:
    """Find the first index of a target value in a list."""
    for index, element in enumerate(_items):
        if element == _target:
            return index
    return -1


def test() -> None:
    """Simple self-test for Linear Search."""
    cases = [
        (([10, 20, 30, 40, 50], 30), 2),
        (([1, 2, 3, 4, 5], 10), -1),
        (([], 5), -1),
        (([1, 1, 1], 1), 0),
    ]
    for (items, target), expected in cases:
        try:
            res = linear_search(items, target)
            assert res == expected, (
                f"Failed for search {target} in {items}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
