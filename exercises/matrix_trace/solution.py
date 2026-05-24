SUBMIT = True


def matrix_trace(mat: list[list[int | float]]) -> int | float:
    #ahora que lo pienso , lo que hice fue un for 😅
    solution =mat[0][0]
    i = 1
    while i != len(mat): 
        solution += mat[i][i]
        i+=1
    return solution  


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
