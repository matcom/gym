SUBMIT = True


def personalized_greeting(_name: str, _age: int) -> str:
    # noqa: ARG001
    """Returns a personalized greeting message.

    Example usage:
    >>> personalized_greeting("Alice", 25)
    'Hello Alice, you are 25 years old'
    >>> personalized_greeting("Bob", 30)
    'Hello Bob, you are 30 years old'
    """
    return f"Hello {_name}, you are {_age} years old"


def test() -> None:
    """Simple self-test for Personalized Greeting."""
    cases = [
        (("Alice", 25), "Hello Alice, you are 25 years old"),
        (("Bob", 30), "Hello Bob, you are 30 years old"),
    ]
    for (name, age), expected in cases:
        try:
            res = personalized_greeting(name, age)
            assert res == expected, (
                f"Failed for {name}, {age}: expected '{expected}', got '{res}'"
            )
        except AssertionError as e:
            print(f"❌ {e}")
            return
    print("✅ All tests passed!")


if __name__ == "__main__":
    test()
