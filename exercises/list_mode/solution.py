from typing import Any

SUBMIT = True


def list_mode(_items: list[Any]) -> Any:
    """Returns the most frequent element in a list.

    Example usage:
    >>> list_mode([1, 2, 2, 3, 3, 3])
    3
    >>> list_mode(['a', 'b', 'a'])
    'a'
    """
    if(_items.__len__() <= 0):
        return None
    _map = {}
    for item in _items:
        if item in _map:
            _map[item] += 1
        else:
            _map[item] = 1
    _item, _num = _items[0], _map[_items[0]]
    for item, num in _map.items():
        if(num > _num):
            _item, _num = item, num
    return _item


def test() -> None:
    """Simple self-test for Most Common Element."""
    cases: list[tuple[list[Any], Any]] = [
        ([1, 2, 2, 3, 3, 3], 3),
        (["a", "b", "a"], "a"),
        ([10], 10),
    ]
    for items, expected in cases:
        try:
            res = list_mode(items)
            assert res == expected, (
                f"Failed for {items}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
