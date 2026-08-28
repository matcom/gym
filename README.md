# matcom-gym

Coding gym for MatCom students. CLI-first, test-driven feedback, local-only
progress. Ships with 25 exercises across 8 topics (básico, condicionales,
ciclos, strings, listas, diccionarios, funciones, recursión), each with a
canonical solution you can peek at.

> **Note.** This is a fresh v1 rewrite. The previous fork-and-PR flow is
> preserved on the [`legacy-v0`](https://github.com/matcom/gym/tree/legacy-v0)
> branch.

## Install

```bash
pipx install matcom-gym
# or, without installing:
uvx matcom-gym
```

## Usa la gym

Al correr `matcom-gym` por primera vez te pide nombre y grupo (se guarda en
`~/.matcom-gym/profile.json`). Después:

```bash
matcom-gym list                    # todos los ejercicios
matcom-gym list -t strings         # filtra por tema
matcom-gym start count_vowels      # copia el ejercicio a ~/matcom-gym/ y
                                   # abre solution.py en tu editor
# ...editás la solución...
matcom-gym evaluar count_vowels    # corre los buckets y te dice qué falla
matcom-gym peek count_vowels       # muestra la solución canónica comentada
matcom-gym progreso                # cuántos llevas resueltos
```

### Cómo funciona el feedback

Cada ejercicio tiene "buckets" de tests agrupados por *tipo de error* —
`basic`, `edge_empty`, `edge_case`, `edge_accents`, etc. Cuando falla un
bucket, la gym te dice **qué familia de casos** estás olvidando (no el input
exacto). Ejemplo con `count_vowels` mal resuelto:

```
❌ bucket basic          → revisa los casos con vocales normales en minúscula
✅ bucket edge_empty
❌ bucket edge_case      → las mayúsculas también son vocales (A, E, I, O, U)
❌ bucket edge_accents   → las vocales acentuadas del español cuentan
```

### Editor

`matcom-gym start` abre `solution.py` con `$EDITOR`, o `code`, o
`xdg-open`, en ese orden. Si ninguno está disponible, imprime la ruta.

### Dónde vive lo tuyo

- Ejercicios materializados: `~/matcom-gym/<tema>/<slug>/`
- Perfil e intentos: `~/.matcom-gym/`

Ambos son sobreescribibles vía `$MATCOM_GYM_HOME` y `$MATCOM_GYM_STATE_DIR`
(útil para tests o para tener varias "sesiones" separadas).

## Contenido

25 ejercicios, cada uno con:
- `README.md` — enunciado en español
- `template.py` — esqueleto para empezar
- `examples.py` — 2-3 ejemplos ilustrativos
- `canonical.py` — solución de referencia (peek)
- `tests/bucket_*.py` — casos agrupados por tipo de error
- `wrong_solutions.py` — soluciones rotas típicas (usadas por el suite de
  meta-tests para verificar que cada bucket es discriminante)

## Roadmap

- ✅ M0 — Skeleton
- ✅ M1 — Un ejercicio end-to-end
- ✅ M2 — Catalog + local state
- ✅ M3 — 25 ejercicios + meta-tests que garantizan que los buckets discriminan
- ✅ M5 — Empaquetado (`pipx` / `uvx`)
- ⬜ M4 — TUI dashboard (textual)
- ⬜ Lecturas cortas por tema

Diseño completo: `Atlas/Architecture/2026-08-27-matcom-gym-design.md` en el
workspace vault.

## Desarrollo

```bash
uv sync --all-groups
uv run pytest            # 192 tests: CLI, evaluator, canonical, buckets discriminantes
uv run ruff check .
uv run matcom-gym
```

## License

MIT.
