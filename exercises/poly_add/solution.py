SUBMIT = True


def poly_add(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Adds two polynomials."""
    poly_min, poly_max = None, None
    if(len(poly1) > len(poly2)):
        poly_min, poly_max = poly2, poly1[:]
    else:
        poly_min, poly_max = poly1, poly2[:]
    offset = len(poly_max) - len(poly_min)
    for i in range(len(poly_min)):
        poly_max[offset + i] += poly_min[i]
    return poly_max


def test() -> None:
    """Simple self-test for Polynomial Addition."""
    cases = [(([1, 2], [3, 4]), [4, 6]), (([1, 0, 1], [1, 1]), [1, 1, 2])]
    for input_data, expected in cases:
        try:
            res = poly_add(*input_data)
            assert res == expected, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
