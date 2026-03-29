SUBMIT = True


def matrix_add(mat1: list[list[int | float]], mat2: list[list[int | float]]) -> list[list[int | float]]:
    """Adds two matrices."""
    # Placeholder implementation
    _ = mat1
    _ = mat2
   
    for i in range (len(mat2)):
        mat1[i] += mat2[i]

    return mat1


def test() -> None:
    """Simple self-test for Matrix Addition."""
    cases = [(([1, 2], [3, 4]), [4, 6])]  # Example matrices
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
