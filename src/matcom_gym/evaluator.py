"""Ejecuta los buckets ocultos contra el solution.py del estudiante.

Cada bucket es un módulo con `run()` que hace asserts. Un bucket "pasa"
si run() no lanza. El feedback combina los hints de los buckets fallidos.
"""

from __future__ import annotations

import importlib.util
import sys
from dataclasses import dataclass
from pathlib import Path

from matcom_gym.catalog import Exercise
from matcom_gym.materialize import student_dir


@dataclass
class BucketResult:
    name: str
    ok: bool
    error: str | None
    hint: str


@dataclass
class EvalReport:
    slug: str
    results: list[BucketResult]

    @property
    def ok_count(self) -> int:
        return sum(1 for r in self.results if r.ok)

    @property
    def all_ok(self) -> bool:
        return bool(self.results) and all(r.ok for r in self.results)


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def evaluate(ex: Exercise) -> EvalReport:
    stu_dir = student_dir(ex)
    solution_path = stu_dir / "solution.py"
    if not solution_path.exists():
        raise FileNotFoundError(
            f"No hay solution.py en {stu_dir}. Corre `matcom-gym start {ex.slug}` primero."
        )

    # Hacemos importable el directorio del estudiante para que los buckets
    # puedan `from solution import ...`. Limpiamos al final por si estamos
    # dentro del mismo proceso (test suite).
    sys.path.insert(0, str(stu_dir))
    sys.modules.pop("solution", None)

    results: list[BucketResult] = []
    try:
        tests_dir = ex.path / "tests"
        for bucket_meta in ex.buckets:
            name = bucket_meta["name"]
            hint = bucket_meta.get("hint", "")
            bucket_path = tests_dir / f"bucket_{name}.py"
            if not bucket_path.exists():
                results.append(
                    BucketResult(name, False, f"falta el archivo {bucket_path.name}", hint)
                )
                continue
            try:
                mod = _load_module(f"_gym_bucket_{name}", bucket_path)
                mod.run()
                results.append(BucketResult(name, True, None, hint))
            except AssertionError as e:
                results.append(BucketResult(name, False, str(e) or "assertion falló", hint))
            except Exception as e:
                results.append(BucketResult(name, False, f"{type(e).__name__}: {e}", hint))
    finally:
        if str(stu_dir) in sys.path:
            sys.path.remove(str(stu_dir))
        sys.modules.pop("solution", None)

    return EvalReport(slug=ex.slug, results=results)
