SUBMIT = True


def sum_list_recursive(lst: list[int]) -> int:
    if not lst:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])#bien phyton con el slice 


def test() -> None:
    """Simple self-test for Recursive List Sum."""
    cases = [([1, 2, 3, 4], 10), ([], 0), ([5], 5), ([-1, 1, -2, 2], 0)]
    for items, expected in cases:
        try:
            res = sum_list_recursive(items)
            assert res == expected, (
                f"Failed for {items}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
