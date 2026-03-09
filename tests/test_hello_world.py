import pytest

from exercises.hello_world import solution
from exercises.hello_world.solution import hello_world

if not getattr(solution, "SUBMIT", False):
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_hello_world_exists() -> None:
    assert callable(hello_world)
