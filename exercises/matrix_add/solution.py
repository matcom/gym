SUBMIT = True


def matrix_add(mat1: list[list[int | float]], mat2: list[list[int | float]]) -> list[list[int | float]]:
    """Adds two matrices."""
    
    
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            mat1[i][j] += mat2[i][j]
    return mat1


def test() -> None:
    """Simple self-test for Matrix Addition."""
    cases = [
    (([[1, 2]], [[3, 4]]), [[4, 6]]),               # 1x2
    (([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]]),  # 2x2
    (([[1]], [[9]]), [[10]])                         # 1x1 a añadi mas casitos de pruebas y arregle el anterior 
]

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
