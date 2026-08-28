"""Meta-tests sobre el contenido.

Dos invariantes:
1. Cada canonical pasa todos sus propios buckets.
2. Cada bucket es discriminante: para cada `(bucket, wrong_fn)` declarado
   en `wrong_solutions.TARGETS`, al evaluar esa función rota el bucket
   nombrado aparece en `failed`.
"""

import importlib.util
import inspect

import pytest

from matcom_gym import catalog, materialize
from matcom_gym.evaluator import evaluate


@pytest.fixture
def isolated_gym(tmp_path, monkeypatch):
    monkeypatch.setenv("MATCOM_GYM_HOME", str(tmp_path / "gym-home"))
    monkeypatch.setenv("MATCOM_GYM_STATE_DIR", str(tmp_path / "state"))
    yield tmp_path


def _public_name(ex) -> str:
    # signature ejemplo: "def count_vowels(text: str) -> int"
    return ex.signature.split("def ", 1)[1].split("(", 1)[0].strip()


def _load_wrong_solutions(ex):
    path = ex.path / "wrong_solutions.py"
    if not path.exists():
        return None
    spec = importlib.util.spec_from_file_location(
        f"wrong_solutions_{ex.slug}", path
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _fn_as_solution(fn, public_name: str) -> str:
    """Reescribe el source de fn con el nombre público del ejercicio."""
    src = inspect.getsource(fn)
    # inspect.getsource conserva el nombre original en `def <name>(...)`.
    # Renombramos solo esa primera aparición para no tocar el cuerpo.
    return src.replace(f"def {fn.__name__}(", f"def {public_name}(", 1)


@pytest.mark.parametrize("ex", catalog.all_exercises(), ids=lambda e: e.slug)
def test_canonical_passes_own_buckets(ex, isolated_gym):
    dest = materialize.materialize(ex)
    canonical = (ex.path / "canonical.py").read_text(encoding="utf-8")
    (dest / "solution.py").write_text(canonical)
    report = evaluate(ex)
    failed = [(r.name, r.error) for r in report.results if not r.ok]
    assert report.all_ok, f"{ex.slug}: fallaron {failed}"


def _wrong_solution_cases():
    cases = []
    for ex in catalog.all_exercises():
        mod = _load_wrong_solutions(ex)
        if mod is None:
            continue
        for bucket_name, fns in mod.TARGETS.items():
            for fn in fns:
                cases.append(
                    pytest.param(
                        ex, bucket_name, fn,
                        id=f"{ex.slug}::{bucket_name}::{fn.__name__}",
                    )
                )
    return cases


@pytest.mark.parametrize("ex,bucket_name,fn", _wrong_solution_cases())
def test_wrong_solution_fails_targeted_bucket(ex, bucket_name, fn, isolated_gym):
    dest = materialize.materialize(ex)
    (dest / "solution.py").write_text(_fn_as_solution(fn, _public_name(ex)))
    report = evaluate(ex)
    failed = {r.name for r in report.results if not r.ok}
    assert bucket_name in failed, (
        f"{ex.slug}: la solución rota `{fn.__name__}` debía hacer fallar "
        f"el bucket `{bucket_name}` pero pasó. Buckets que fallaron: {failed}"
    )
