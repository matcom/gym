SUBMIT = True

#hice algunos cambios en la definicion de la funcion porque el low inicializaba en 0 y bueno pueden existir valores negativos 
def recursive_min_max(lst: list[int], low: int | None = None, high: int | None = None) -> tuple[int, int]:
    if not lst:
        return (low, high)
    
    first = lst[0]
    if low is None or first < low:
        low = first
    if high is None or first > high:
        high = first
    
    return recursive_min_max(lst[1:], low, high)

def test() -> None:
    """Simple self-test for Recursive Min/Max."""
    assert recursive_min_max([3, 1, 4, 1, 5, 9]) == (1, 9), (
        f"Expected (1, 9), got {recursive_min_max([3, 1, 4, 1, 5, 9])}"
    )
    assert recursive_min_max([42]) == (42, 42), (
        f"Expected (42, 42), got {recursive_min_max([42])}"
    )
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
