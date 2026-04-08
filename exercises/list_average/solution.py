SUBMIT = True


def list_average(_numbers: list[float]) -> float:
    """Returns the mean of a numeric list.

    Example usage:
    >>> list_average([1, 2, 3, 4, 5])
    2.5
    >>> list_average([10, 20, 30])
    20.0
    """
    promedio = 0
    for c in _numbers :
        promedio +=c

    resultado = promedio / len(_numbers)
    return resultado


def test() -> None:
    """Simple self-test for Computing Average."""
    cases = [([1, 2, 3, 4, 5], 3.0), ([10, 20, 30], 20.0), ([5], 5.0)]
    for nums, expected in cases:
        try:
            res = list_average([float(x) for x in nums])
            assert abs(res - expected) < 1e-9, (
                f"Failed for {nums}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
