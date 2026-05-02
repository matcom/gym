SUBMIT = True


def poly_add(poly1: list[int | float], poly2: list[int | float]) -> list[int | float]:
    """Adds two polynomials."""
    
    if len(poly1) < len(poly2):
        temp = [0] * (len(poly2) - len(poly1))
        temp.extend(poly1)
        poly1 = temp
        
    elif len(poly2) < len(poly1):
        temp = [0] * (len(poly1) - len(poly2))
        temp.extend(poly2)
        poly2 = temp
    
    new_poly = []
    for i in range(len(poly1)):
        new_poly.append(poly1[i]+poly2[i])
    return new_poly

def test() -> None:
    """Simple self-test for Polynomial Addition."""
    cases = [(([1, 2], [3, 4]), [4, 6]), (([1, 0, 1], [1, 1]), [1, 1, 2])]
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
