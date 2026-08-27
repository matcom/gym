from typer.testing import CliRunner

from matcom_gym import __version__
from matcom_gym.cli import app

runner = CliRunner()


def test_default_prints_placeholder() -> None:
    result = runner.invoke(app, [])
    assert result.exit_code == 0
    assert "matcom-gym" in result.stdout


def test_version_matches_package() -> None:
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_hola_uses_provided_name() -> None:
    result = runner.invoke(app, ["hola", "--nombre", "Alex"])
    assert result.exit_code == 0
    assert "Alex" in result.stdout
