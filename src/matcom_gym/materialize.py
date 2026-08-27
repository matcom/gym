"""Materializa un ejercicio en la carpeta del estudiante.

Copia template.py → solution.py, examples.py y README.md a
~/matcom-gym/<topic>/<slug>/. Nunca pisa un solution.py existente.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

from matcom_gym.catalog import Exercise


def _gym_home() -> Path:
    override = os.environ.get("MATCOM_GYM_HOME")
    return Path(override) if override else Path.home() / "matcom-gym"


def student_dir(ex: Exercise) -> Path:
    return _gym_home() / ex.topic / ex.slug


def materialize(ex: Exercise, *, overwrite: bool = False) -> Path:
    dest = student_dir(ex)
    dest.mkdir(parents=True, exist_ok=True)
    mapping = [
        ("template.py", "solution.py"),
        ("examples.py", "examples.py"),
        ("README.md", "README.md"),
    ]
    for src_name, target_name in mapping:
        src = ex.path / src_name
        if not src.exists():
            continue
        target = dest / target_name
        # Nunca clobbeamos el trabajo del estudiante.
        if target_name == "solution.py" and target.exists() and not overwrite:
            continue
        shutil.copy2(src, target)
    return dest
