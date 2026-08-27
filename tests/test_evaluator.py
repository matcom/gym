"""Tests end-to-end del evaluator sobre count_vowels."""


import pytest

from matcom_gym import catalog, materialize


@pytest.fixture
def isolated_gym(tmp_path, monkeypatch):
    monkeypatch.setenv("MATCOM_GYM_HOME", str(tmp_path / "gym-home"))
    monkeypatch.setenv("MATCOM_GYM_STATE_DIR", str(tmp_path / "state"))
    yield tmp_path


def test_catalog_finds_count_vowels():
    ex = catalog.find("count_vowels")
    assert ex is not None
    assert ex.topic == "strings"
    assert len(ex.buckets) == 4
    assert {b["name"] for b in ex.buckets} == {"basic", "edge_empty", "edge_case", "edge_accents"}


def test_materialize_creates_solution(isolated_gym):
    ex = catalog.find("count_vowels")
    dest = materialize.materialize(ex)
    assert (dest / "solution.py").exists()
    assert (dest / "examples.py").exists()
    assert (dest / "README.md").exists()
    # canonical NO se copia
    assert not (dest / "canonical.py").exists()
    # tests NO se copian
    assert not (dest / "tests").exists()


def test_materialize_does_not_clobber_student_work(isolated_gym):
    ex = catalog.find("count_vowels")
    dest = materialize.materialize(ex)
    (dest / "solution.py").write_text("# mi trabajo\n")
    materialize.materialize(ex)  # segundo run
    assert (dest / "solution.py").read_text() == "# mi trabajo\n"


def test_evaluator_all_ok_with_canonical(isolated_gym):
    from matcom_gym.evaluator import evaluate

    ex = catalog.find("count_vowels")
    dest = materialize.materialize(ex)
    # Reemplazamos el template vacío con la solución canónica.
    canonical = (ex.path / "canonical.py").read_text(encoding="utf-8")
    (dest / "solution.py").write_text(canonical)

    report = evaluate(ex)
    assert report.all_ok
    assert report.ok_count == 4


def test_evaluator_reports_failed_buckets_with_broken_solution(isolated_gym):
    from matcom_gym.evaluator import evaluate

    ex = catalog.find("count_vowels")
    dest = materialize.materialize(ex)
    # Solución rota: solo cuenta minúsculas simples sin acentos.
    (dest / "solution.py").write_text(
        "def count_vowels(text):\n"
        "    return sum(1 for c in text if c in 'aeiou')\n"
    )
    report = evaluate(ex)
    assert not report.all_ok
    failed = {r.name for r in report.results if not r.ok}
    # No cuenta mayúsculas ni acentos
    assert "edge_case" in failed
    assert "edge_accents" in failed
    # Sí cuenta los básicos y el vacío
    ok = {r.name for r in report.results if r.ok}
    assert "basic" in ok
    assert "edge_empty" in ok


def test_evaluator_raises_when_no_solution(isolated_gym):
    from matcom_gym.evaluator import evaluate

    ex = catalog.find("count_vowels")
    with pytest.raises(FileNotFoundError):
        evaluate(ex)
