import ast
from pathlib import Path
#y aqui le puse lo del submit , no se si realmente pinche pero ahi esta 
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

# funcion para contar las vocales
def count_vowels(s: str) -> int:
    solution = 0
    vowels = "aeiouAEIOU"
    for i in vowels:
        for j in s:
            if i == j:
                solution+=1
    return solution
'''no se muy bien como pincha lo d arriba pero hice mi propio metodo test
me fije un poco por los ejercicios anteriores 
pase mas trabajo en esto que en haciendo el ejercicio jjj😅'''
def test():
    try:
        assert count_vowels("hello") == 2
        assert count_vowels("HELLO") == 2
        assert count_vowels("xyz") == 0
        assert count_vowels("aeiou") == 5
        assert count_vowels("123124") == 0
        print("✅ Todas las pruebas pasaron. Tu función está bien.")
    except AssertionError:
        print("❌ Alguna prueba falló. Revisa tu función.")

if __name__ == "__main__":
    test()
