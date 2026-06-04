SUBMIT = True


def binary_search_recursive(
    lst: list[int], target: int, low: int = 0, high: int | None = None
) -> int:
    if(high is None): 
        high = len(lst) - 1

    if(low > high): 
        return -1
    
    mid = (low + high) // 2
    if(lst[mid] == target):
        return mid
    elif(lst[mid] < target):
        return binary_search_recursive(lst, target, low, mid - 1)
    else:
        return binary_search_recursive(lst, target, mid + 1, high)


def test() -> None:
    """Simple self-test for Recursive Binary Search."""
    assert binary_search_recursive([1, 2, 3, 4, 5], 3) == 2, (
        f"Expected 2, got {binary_search_recursive([1, 2, 3, 4, 5], 3)}"
    )
    assert binary_search_recursive([1, 2, 3, 4, 5], 6) == -1, (
        f"Expected -1, got {binary_search_recursive([1, 2, 3, 4, 5], 6)}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
