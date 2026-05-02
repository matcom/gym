from typing import Any

SUBMIT = True


def list_mode(_items: list[Any]) -> Any:
    """Returns the most frequent element in a list."""
    if not _items:
        return None
    elements = {}.fromkeys(_items, 0)
    
    for item in _items:
        elements[item] += 1
    
    num = max(elements.values())
    
    for key, value in elements.items():
        if value == num:
            return key


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
