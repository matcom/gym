SUBMIT = True


def poly_evaluate(poly: list[int | float], x: int | float) -> int | float:
    """Evaluates a polynomial at a given value x using Horner's method."""
    count = 0
    for i in range(len(poly)-1, -1, -1):
        count += poly[i] * (x**i)
    
    return count

def test() -> None:
    """Simple self-test for Polynomial Evaluation."""
    cases = [(([1, 2, 3], 2), 17), (([5], 3), 5), ([], 0), (([1, -1, 1], 1), 1)]
    for input_data, expected in cases:
        try:
            res = poly_evaluate(*input_data)
            assert abs(res - expected) < 1e-9, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
