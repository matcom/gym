import ast
from pathlib import Path
SUBMIT = True
def test_exercise_solutions_have_asserts() -> None:
    """Verify that all exercise solution stubs have a test() function with asserts."""
    root = Path(__file__).parent.parent
    exercises_dir = root / "exercises"

    exercises = [
        d
        for d in exercises_dir.iterdir()
        if d.is_dir() and not d.name.startswith((".", "__"))
    ]

    for exercise in exercises:
        solution_path = exercise / "solution.py"
        assert solution_path.exists(), f"Missing solution.py in {exercise.name}"

        tree = ast.parse(solution_path.read_text())
        test_func = None
        for node in tree.body:
            if isinstance(node, ast.FunctionDef) and node.name == "test":
                test_func = node
                break

        assert test_func is not None, f"Missing test() function in {exercise.name}"

        # Look for at least one assert statement inside test()
        has_assert = False
        for subnode in ast.walk(test_func):
            if isinstance(subnode, ast.Assert):
                has_assert = True
                break

        assert has_assert, (
            f"test() function in {exercise.name} missing assert statement"
        )
def matrix_mul(mat1, mat2):
    #creamos una matriz de 0 con la cantidad de filas de mat1 y con la cantidad de columnas de 
    solution = [[0 for i in range(len(mat2[0]))]for i in range(len(mat1))]
    
    for i in range(len(mat1)):#recorremos las filas de la primera 
        for j in range (len(mat2[0])):#recorremos las columnas de la segunda 
            for k in range(len(mat1[0])):#recorremos las columnas de la primera 
                solution[i][j] += mat1[i][k] * mat2[k][j]#se multiplican los elementos en comun y se van sumando        
    return solution
#me fije de los testers de otros ejercicios para poder hacerme este porque no estaba 
def test():
    # Caso 1: ejemplo clásico 2x2
    assert matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]], \
        "Multiplicación 2x2 falló"

    # Caso 2: identidad
    assert matrix_mul([[1, 0], [0, 1]], [[9, 8], [7, 6]]) == [[9, 8], [7, 6]], \
        "Multiplicación con identidad falló"

    # Caso 3: valores negativos
    assert matrix_mul([[2, -1]], [[4], [3]]) == [[5]], \
        "Multiplicación con negativos falló"

    # Caso 4: matrices rectangulares 2x3 * 3x2
    mat1 = [[1, 2, 3], [4, 5, 6]]
    mat2 = [[7, 8], [9, 10], [11, 12]]
    expected = [[58, 64], [139, 154]]
    assert matrix_mul(mat1, mat2) == expected, "Multiplicación rectangular falló"

    print("✅ Todas las pruebas pasaron correctamente")

if __name__ == "__main__":
    test()
