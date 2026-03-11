SUBMIT = True


def matrix_trace(mat: list[list[int | float]]) -> int | float:
    """Calculates the trace of a square matrix."""
    trace = 0
    for i in range(len(mat)):
        trace += mat[i][i]
    return trace


def test() -> None:
    """Simple self-test for Matrix Trace."""
    cases = [
        ([[1, 2], [3, 4]], 5),  # 2x2 matrix
        ([[1]], 1),  # 1x1 matrix
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15),  # 3x3 matrix
        ([[-1, -2], [-3, -4]], -5),  # Negative numbers
    ]
    for matrix, expected in cases:
        try:
            res = matrix_trace(matrix)
            assert abs(res - expected) < 1e-9, (
                f"Failed for matrix={matrix}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
