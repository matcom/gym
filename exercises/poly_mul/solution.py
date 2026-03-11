SUBMIT = True


def poly_mul(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Multiplies two polynomials."""
    n1, n2 = len(poly1), len(poly2)
    poly = [0] * (n1 + n2 - 1)
    for i, v1 in enumerate(poly1):
        for j, v2 in enumerate(poly2):
            poly[i + j] += v1 * v2
    return poly


def test() -> None:
    """Simple self-test for Polynomial Multiplication."""
    cases = [
        (([1, 2], [3, 4]), [3, 10, 8]),
        (([1, 0, 1], [1, 1]), [1, 1, 1, 1]),
    ]
    for input_data, expected in cases:
        try:
            res = poly_mul(*input_data)
            assert res == expected, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
