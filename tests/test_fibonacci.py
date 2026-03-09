import pytest

from exercises.fibonacci import solution
from exercises.fibonacci.solution import fibonacci

if not getattr(solution, "SUBMIT", False):
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_fibonacci_exists() -> None:
    assert callable(fibonacci)
