SUBMIT = True


def simple_interest(_principal: float, _rate: float, _time: float) -> float:
    # noqa: ARG001
    #Calculates simple interest using the formula: I = (P * R * T) / 100.
     return (_principal * _rate * _time) / 100


def test() -> None:
    """Simple self-test for Simple Interest Calculator."""
    cases = [(1000, 5, 2, 100.0), (500, 3.5, 1, 17.5)]
    for p, r, t, expected in cases:
        try:
            res = simple_interest(float(p), float(r), float(t))
            assert abs(res - expected) < 1e-9, (
                f"Failed for P={p}, R={r}, T={t}: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
