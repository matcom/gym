SUBMIT = True


def matrix_add(mat1: list[list[int | float]], mat2: list[list[int | float]]) -> list[list[int | float]]:
    """Adds two matrices."""
    mat3 = []
    temp = [0] * len(mat1[0])
    for i in range(len(mat1)):
        mat3.append(temp)
    
    for x in range(len(mat1)):
        for y in range(len(mat1[0])):
            mat3[x][y] = mat1[x][y] + mat2[x][y]
    
    return mat3


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
