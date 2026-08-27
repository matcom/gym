"""Catálogo de ejercicios empaquetados con matcom-gym."""

from __future__ import annotations

import json
from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path


@dataclass
class Exercise:
    slug: str
    title: str
    topic: str
    difficulty: str
    signature: str
    tags: list[str]
    buckets: list[dict]
    path: Path  # ubicación en el paquete instalado


def _content_root() -> Path:
    return Path(str(files("matcom_gym"))) / "content" / "exercises"


def all_exercises() -> list[Exercise]:
    root = _content_root()
    out: list[Exercise] = []
    if not root.exists():
        return out
    for topic_dir in sorted(root.iterdir()):
        if not topic_dir.is_dir():
            continue
        for ex_dir in sorted(topic_dir.iterdir()):
            meta_path = ex_dir / "meta.json"
            if not meta_path.exists():
                continue
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
            out.append(
                Exercise(
                    slug=meta["slug"],
                    title=meta["title"],
                    topic=meta["topic"],
                    difficulty=meta.get("difficulty", "unknown"),
                    signature=meta.get("signature", ""),
                    tags=meta.get("tags", []),
                    buckets=meta.get("buckets", []),
                    path=ex_dir,
                )
            )
    return out


def find(slug: str) -> Exercise | None:
    for ex in all_exercises():
        if ex.slug == slug:
            return ex
    return None
