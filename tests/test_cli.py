import os

from typer.testing import CliRunner

from matcom_gym import __version__
from matcom_gym.cli import app

runner = CliRunner()


def _iso_env(tmp_path):
    return {
        **os.environ,
        "MATCOM_GYM_STATE_DIR": str(tmp_path / "state"),
        "MATCOM_GYM_HOME": str(tmp_path / "gym-home"),
    }


def test_default_prints_banner(tmp_path):
    result = runner.invoke(app, [], env=_iso_env(tmp_path))
    assert result.exit_code == 0
    assert "matcom-gym" in result.stdout


def test_version_matches_package(tmp_path):
    result = runner.invoke(app, ["version"], env=_iso_env(tmp_path))
    assert result.exit_code == 0
    assert __version__ in result.stdout


def test_hola_uses_provided_name(tmp_path):
    result = runner.invoke(app, ["hola", "--nombre", "Alex"], env=_iso_env(tmp_path))
    assert result.exit_code == 0
    assert "Alex" in result.stdout


def test_list_shows_count_vowels(tmp_path):
    result = runner.invoke(app, ["list"], env=_iso_env(tmp_path))
    assert result.exit_code == 0
    assert "count_vowels" in result.stdout


def test_peek_prints_canonical(tmp_path):
    result = runner.invoke(app, ["peek", "count_vowels"], env=_iso_env(tmp_path))
    assert result.exit_code == 0
    assert "count_vowels" in result.stdout


def test_peek_unknown_slug(tmp_path):
    result = runner.invoke(app, ["peek", "no_existe"], env=_iso_env(tmp_path))
    assert result.exit_code == 1
