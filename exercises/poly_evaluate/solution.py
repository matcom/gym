SUBMIT = True


def poly_evaluate(poly: list[int | float], x: int | float) -> int | float:
    
    solution = 0
    for i in range(len(poly)) :
        solution += (x**i ) * poly[i] 
        
    return solution


def test() -> None:
    """Simple self-test for Polynomial Evaluation."""
    cases = [(([1, 2, 3], 2), 17), (([5], 3), 5), (([],0),0), (([1, -1, 1], 1), 1)] #tuve que arreglar el tester porque en el caso [] faltaba un argumento
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
