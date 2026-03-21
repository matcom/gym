SUBMIT = False


def binary_search_recursive(
    lst: list[int], target: int, low: int = 0, high: int | None = None
) -> int:
    """Recursive Binary Search"""

    if high is None:
        high = len(lst) - 1 # inicializar variable

    if not lst[low] <= target <= lst[high]:
        return -1   # 4. no encontrado
        
    # 1. cortar a la mitad la lista 
    mid = (low + high)//2    # calculando la mitad
    
    # 2. el valor del medio compararlo con el target y tomar desiciones sobre descartar las sublistas
    if lst[mid] == target:
        return mid   # 3. se encontro, retornar el indice
    elif lst[mid] > target: 
        lst[0:mid]
        return binary_search_recursive(lst, target, low, mid - 1)
    elif lst[mid] < target:
        lst[mid + 1:]
        return binary_search_recursive(lst, target, mid + 1, len(lst) - 1)
    
    return -1   # 4. si no se ha encontrado, retornar -1
 



def test() -> None:
    """Simple self-test for Recursive Binary Search."""
    assert binary_search_recursive([1, 2, 3, 4, 5], 3) == 2, (
        f"Expected 2, got {binary_search_recursive([1, 2, 3, 4, 5], 3)}"
    )
    assert binary_search_recursive([1, 2, 3, 4, 5], 6) == -1, (
        f"Expected -1, got {binary_search_recursive([1, 2, 3, 4, 5], 6)}"
    )
    assert binary_search_recursive([1, 2, 3, 4, 5], 5) == 4, (
        f"Expected 4, got {binary_search_recursive([1, 2, 3, 4, 5], 4)}"
    )
    assert binary_search_recursive([1, 2, 3, 4, 5], 1) == 0, (
        f"Expected 0, got {binary_search_recursive([1, 2, 3, 4, 5], 1)}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
