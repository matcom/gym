"""Meta-tests sobre el contenido: cada canonical pasa sus propios buckets."""

import pytest

from matcom_gym import catalog, materialize
from matcom_gym.evaluator import evaluate


@pytest.fixture
def isolated_gym(tmp_path, monkeypatch):
    monkeypatch.setenv("MATCOM_GYM_HOME", str(tmp_path / "gym-home"))
    monkeypatch.setenv("MATCOM_GYM_STATE_DIR", str(tmp_path / "state"))
    yield tmp_path


@pytest.mark.parametrize("ex", catalog.all_exercises(), ids=lambda e: e.slug)
def test_canonical_passes_own_buckets(ex, isolated_gym):
    dest = materialize.materialize(ex)
    canonical = (ex.path / "canonical.py").read_text(encoding="utf-8")
    (dest / "solution.py").write_text(canonical)
    report = evaluate(ex)
    failed = [(r.name, r.error) for r in report.results if not r.ok]
    assert report.all_ok, f"{ex.slug}: fallaron {failed}"
