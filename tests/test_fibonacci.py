import pytest
from exercises.fibonacci.solution import SUBMIT, fibonacci

if not SUBMIT:
    pytest.skip("Solution not submitted", allow_module_level=True)


def test_fibonacci_exists() -> None:
    assert callable(fibonacci)
