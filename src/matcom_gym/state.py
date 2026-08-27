"""Estado local del estudiante: perfil + intentos.

Vive en ~/.matcom-gym/ como JSON. Esquema versionado para poder migrar
cuando llegue la sincronización con el servidor (fase 2).
"""

from __future__ import annotations

import json
import os
from datetime import UTC, datetime
from pathlib import Path


def _state_dir() -> Path:
    override = os.environ.get("MATCOM_GYM_STATE_DIR")
    return Path(override) if override else Path.home() / ".matcom-gym"


def _profile_path() -> Path:
    return _state_dir() / "profile.json"


def _state_path() -> Path:
    return _state_dir() / "state.json"


def _ensure_dir() -> None:
    _state_dir().mkdir(parents=True, exist_ok=True)


def load_profile() -> dict | None:
    p = _profile_path()
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))


def save_profile(name: str, group: str) -> dict:
    _ensure_dir()
    profile = {
        "name": name,
        "group": group,
        "created": datetime.now(UTC).isoformat(),
    }
    _profile_path().write_text(json.dumps(profile, indent=2, ensure_ascii=False))
    return profile


def load_state() -> dict:
    p = _state_path()
    if not p.exists():
        return {"version": 1, "attempts": []}
    return json.loads(p.read_text(encoding="utf-8"))


def append_attempt(slug: str, buckets_ok: list[str], buckets_fail: list[str]) -> None:
    _ensure_dir()
    state = load_state()
    state["attempts"].append(
        {
            "slug": slug,
            "ts": datetime.now(UTC).isoformat(),
            "buckets_ok": buckets_ok,
            "buckets_fail": buckets_fail,
        }
    )
    _state_path().write_text(json.dumps(state, indent=2, ensure_ascii=False))


def exercise_status(slug: str) -> str:
    """'not_started' | 'in_progress' | 'done'."""
    attempts = [a for a in load_state()["attempts"] if a["slug"] == slug]
    if not attempts:
        return "not_started"
    return "done" if not attempts[-1]["buckets_fail"] else "in_progress"
