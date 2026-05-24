SUBMIT = True

#tuve que añadirle un elemento a la funcion para que me saliese la parte recursiva 
def prefix_sums(_numbers: list[int], current: int = 0) -> list[int]:
    if not _numbers:
        return []
    current += _numbers[0]
    return [current] + prefix_sums(_numbers[1:], current)#aprovechamos que la suma de listas esta definida en phyton asi 
#clase talla 


def test() -> None:
    """Simple self-test for Cumulative Sums."""
    cases = [([1, 2, 3], [1, 3, 6]), ([10, -10, 5], [10, 0, 5])]
    for nums, expected in cases:
        try:
            res = prefix_sums(nums)
            assert res == expected, f"Failed for {nums}: expected {expected}, got {res}"
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
