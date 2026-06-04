SUBMIT = True


def matrix_add(mat1: list[list[int | float]], mat2: list[list[int | float]]) -> list[list[int | float]]:
    """Adds two matrices."""
    # Placeholder implementation
    n = len(mat1)
    m = len(mat1[0])
    mat = [[0] * m] * n
    for i in range(n):
        for j in range(m):
            mat[i][j] = mat1[i][j] + mat2[i][j]
    return mat


def test() -> None:
    """Simple self-test for Matrix Addition."""
    cases = [(([[1, 2]], [[3, 4]]), [[4, 6]])]  # Example matrices
    for input_data, expected in cases:
        try:
            res = matrix_add(*input_data)
            assert res == expected, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
