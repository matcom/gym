SUBMIT = True


def poly_add(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Adds two polynomials."""
    _poly1 = poly1
    _poly2 = poly2
    maxima_longitud = max(len(poly1), len(poly2))
    

    final = [0 for j in range(maxima_longitud)]
    for i in range(len(poly1)) :
        final[i] += poly1[i]
    for j in range(len(poly2)) :
        final[j] += poly2[j]


    
    if final[-1] == 0 :
        final.pop()
    # Placeholder implementation: Add actual logic here.
    # For now, return an empty list to pass initial checks.
    return final


def test() -> None:
    """Simple self-test for Polynomial Addition."""
    cases = [(([1, 2], [3, 4]), [4, 6]), (([1, 0, 1], [1, 1]), [2, 1, 1])]
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
