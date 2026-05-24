SUBMIT = True


def hello_world() -> str:
    
    return "Hello, World!"


def test() -> None:
    """Simple self-test for Hello World."""
    expected = "Hello, World!"
    try:
        res = hello_world()
        assert res == expected, f"Expected '{expected}', got '{res}'"
    except AssertionError as e:
        print(f"❌ {e}")
        return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
