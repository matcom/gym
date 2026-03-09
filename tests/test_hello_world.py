import pytest
from exercises.hello_world.solution import SUBMIT, hello_world

if not SUBMIT:
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_hello_world_exists() -> None:
    assert callable(hello_world)
