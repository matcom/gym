SUBMIT = True


def celsius_to_fahrenheit(_celsius: float) -> float:
    
    return (_celsius * 9/5) + 32


def test() -> None:
    """Simple self-test for Temperature Conversion."""
    cases = {0: 32.0, 100: 212.0, -40: -40.0}
    for c, expected in cases.items():
        try:
            res = celsius_to_fahrenheit(float(c))
            assert abs(res - expected) < 1e-9, (
                f"Failed for {c}C: expected {expected}, got {res}"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
