from exercises.hello_world.solution import hello_world


def test_hello_world_exists():
    assert callable(hello_world), "The function 'hello_world' is not defined."


def test_hello_world_returns_string():
    # This will fail initially because the stub returns None
    pass
