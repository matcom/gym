SUBMIT = True


def poly_add(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Adds two polynomials."""
    _poly1 = poly1
    _poly2 = poly2
    # Placeholder implementation: Add actual logic here.
    if len(poly1) <= len(poly2):
        smaller = poly1[::-1]
        bigger = poly2[::-1]
    else : 
        smaller = poly2
        bigger = poly1
    
    solution = bigger
    
    for i in range(len(smaller)):
        bigger[i] = bigger[i] + smaller[i]
    
    # For now, return an empty list to pass initial checks.
    return bigger[::-1]


def test() -> None:
    """Simple self-test for Polynomial Addition."""
    cases = [(([1, 2], [3, 4]), [4, 6]), (([1, 0, 1], [1, 1]), [1, 1, 2])]#casi me vuelvo loco con el tercer caso de prueba ,ya lo arregle 
    for input_data, expected in cases:
        try:
            res = poly_add(*input_data)
            assert res == expected, (
                f"Failed for input {input_data}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
