SUBMIT = False


def celsius_to_fahrenheit(_celsius: float) -> float:
    # noqa: ARG001
    """Converts Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32.

    Example usage:
    >>> celsius_to_fahrenheit(0)
    32.0
    >>> celsius_to_fahrenheit(100)
    212.0
    >>> celsius_to_fahrenheit(-40)  
    -40.0
    """

    # F(0) = 32
    # F(1) = 32 + 9/5 = F(0) + 9/5
    # F(2) = F(1) + 9/5 = 32 + 2*9/5
    # F(n) = F(n-1) + 9/5 = 32 + n*9/5  forma recursiva

    if _celsius == 0:
        return 32.0
    
    elif _celsius < 0:
        return celsius_to_fahrenheit(_celsius + 1) - 9/5
    
    else:
        return celsius_to_fahrenheit(_celsius - 1) + 9/5



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
