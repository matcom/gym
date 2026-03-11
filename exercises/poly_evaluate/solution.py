SUBMIT = True


def poly_evaluate(poly: list[int | float], x: int | float) -> int | float:
    """Evaluates a polynomial at a given value x using Horner's method."""
    result = 0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result


def test() -> None:
    """Simple self-test for Polynomial Evaluation."""
    cases = [(([1, 2, 3], 2), 17), (([5], 3), 5), (([], 0), 0), (([1, -1, 1], 1), 1)]
    for input_data, expected in cases:
        try:
            res = poly_evaluate(input_data[0], input_data[1])
            assert abs(res - expected) < 1e-9, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
