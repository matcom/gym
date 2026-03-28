import ast
from pathlib import Path

def count_vowels_rec(s: str, index: int, cant: int):
    if index == len(s):
        return cant
    
    current_char = s[index].lower()
    if not (current_char == 'a' or 
        current_char == 'e' or 
        current_char == 'i' or
        current_char == 'o' or current_char == 'u'):
        return count_vowels_rec(s, index + 1, cant)
    
    return count_vowels_rec(s, index + 1, cant + 1)

def count_vowels(s: str):
    """ Returns the number of vowels (both uppercase and lowercase) in a given string. """
    return count_vowels_rec(s, 0, 0)


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

# Add a test function with an assert for count_vowels
def test():
    # Example: assert count_vowels("hello") == 2
    assert count_vowels("hello") == 2, (f"expected 2, got: {count_vowels("hello")}")
    assert count_vowels("mississipi") == 4, (f"expected 4, got: {count_vowels("mississipi")}")
    assert count_vowels("AEIOU") == 5, (f"expected 5, got: {count_vowels("AEIOU")}")
    assert count_vowels("AeEeiOU") == 7, (f"expected 7, got: {count_vowels("AeEeiOU")}")
    print ("All test passed")
    
if __name__ == "__main__":
    test()

