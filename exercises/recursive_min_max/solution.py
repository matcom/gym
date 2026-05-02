SUBMIT = True


def recursive_min_max(
    lst: list[int], low: int = 0, high: int | None = None
) -> tuple[int, int]:
    if len(lst) == 0 :
        return None, None

    if len(lst) == 1 :
        return lst[0], lst[0]
    
    medio = len(lst) // 2
    mins, maxs = recursive_min_max(lst[:medio])
    mink, mas = recursive_min_max(lst[medio:])
    maximo = max(maxs, mas)
    minimo = min(mins, mink)  
    return minimo, maximo
   
   


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
