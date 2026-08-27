"""matcom-gym CLI."""

from __future__ import annotations

import os
import shutil as _shutil
import subprocess
import sys as _sys
from pathlib import Path

import typer
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table

from matcom_gym import __version__, catalog, state
from matcom_gym import materialize as mat
from matcom_gym.evaluator import evaluate

app = typer.Typer(
    name="matcom-gym",
    help="Coding gym for MatCom students.",
    no_args_is_help=False,
)
console = Console()

_STATUS_MARKS = {"not_started": "○", "in_progress": "◐", "done": "✓"}


def _open_in_editor(path: Path) -> None:
    editor = os.environ.get("EDITOR")
    if editor:
        subprocess.Popen([editor, str(path)])
        return
    if _shutil.which("code"):
        subprocess.Popen(["code", str(path)])
        return
    if _shutil.which("xdg-open"):
        subprocess.Popen(["xdg-open", str(path)])
        return
    console.print(f"[yellow]Sin editor detectado. Abre a mano:[/] {path}")


def _register_interactively() -> dict:
    console.print("[bold cyan]Bienvenido a matcom-gym.[/] Necesito registrarte.")
    name = typer.prompt("¿Cómo te llamas?")
    group = typer.prompt("¿Cuál es tu grupo?")
    profile = state.save_profile(name, group)
    console.print(f"[green]Registrado.[/] Hola, {name} ({group}).")
    return profile


def _ensure_registered() -> dict:
    profile = state.load_profile()
    if profile:
        return profile
    return _register_interactively()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is not None:
        return
    # En tty: registrar si hace falta y saludar. En no-tty (pipes, tests):
    # sólo el banner.
    if _sys.stdin.isatty() and not state.load_profile():
        _register_interactively()
    profile = state.load_profile()
    if profile:
        console.print(f"[bold cyan]Hola, {profile['name']} ({profile['group']}).[/]")
    else:
        console.print("[bold cyan]matcom-gym[/]")
    console.print("Comandos: [dim]list, start, evaluar, peek, progreso, --help[/]")
    console.print("[dim]Dashboard TUI llega en M4.[/]")


@app.command()
def version() -> None:
    """Imprime la versión instalada."""
    console.print(f"matcom-gym {__version__}")


@app.command("list")
def list_exercises(
    topic: str | None = typer.Option(None, "--topic", "-t", help="Filtra por tema."),
) -> None:
    """Lista los ejercicios disponibles."""
    exs = catalog.all_exercises()
    if topic:
        exs = [e for e in exs if e.topic == topic]
    if not exs:
        console.print("[dim]No hay ejercicios que mostrar.[/]")
        return
    table = Table(title="Ejercicios")
    table.add_column("")
    table.add_column("Tema")
    table.add_column("Slug")
    table.add_column("Título")
    table.add_column("Dif.")
    for ex in exs:
        table.add_row(
            _STATUS_MARKS[state.exercise_status(ex.slug)],
            ex.topic,
            ex.slug,
            ex.title,
            ex.difficulty,
        )
    console.print(table)


@app.command()
def start(slug: str) -> None:
    """Materialisa el ejercicio en ~/matcom-gym/ y abre el editor."""
    if _sys.stdin.isatty():
        _ensure_registered()
    ex = catalog.find(slug)
    if not ex:
        console.print(f"[red]No conozco el ejercicio '{slug}'.[/] Prueba `matcom-gym list`.")
        raise typer.Exit(1)
    dest = mat.materialize(ex)
    solution = dest / "solution.py"
    console.print(f"[green]Listo.[/] Editá: [cyan]{solution}[/]")
    console.print("[dim]Cuando estés listo: `matcom-gym evaluar " + ex.slug + "`[/]")
    _open_in_editor(solution)


@app.command()
def evaluar(slug: str) -> None:
    """Corre los buckets ocultos y da feedback."""
    ex = catalog.find(slug)
    if not ex:
        console.print(f"[red]No conozco el ejercicio '{slug}'.[/]")
        raise typer.Exit(1)
    try:
        report = evaluate(ex)
    except FileNotFoundError as e:
        console.print(f"[red]{e}[/]")
        raise typer.Exit(1) from None

    for r in report.results:
        icon = "[green]✅[/]" if r.ok else "[red]❌[/]"
        console.print(f"  {icon} bucket [bold]{r.name}[/]")
        if not r.ok and r.error:
            console.print(f"     [dim]{r.error}[/]")

    state.append_attempt(
        slug=ex.slug,
        buckets_ok=[r.name for r in report.results if r.ok],
        buckets_fail=[r.name for r in report.results if not r.ok],
    )

    total = len(report.results)
    if report.all_ok:
        console.print(f"\n[bold green]🎉 {report.ok_count}/{total} — ejercicio resuelto.[/]")
    else:
        console.print(f"\n[yellow]{report.ok_count}/{total} buckets ok.[/]")
        for r in report.results:
            if not r.ok and r.hint:
                console.print(f"  → [italic]{r.hint}[/]")


@app.command()
def peek(slug: str) -> None:
    """Muestra la solución canónica bien comentada."""
    ex = catalog.find(slug)
    if not ex:
        console.print(f"[red]No conozco el ejercicio '{slug}'.[/]")
        raise typer.Exit(1)
    canonical = ex.path / "canonical.py"
    if not canonical.exists():
        console.print(f"[yellow]Sin solución canónica para '{slug}'.[/]")
        raise typer.Exit(1)
    syntax = Syntax(
        canonical.read_text(encoding="utf-8"),
        "python",
        theme="monokai",
        line_numbers=True,
    )
    console.print(syntax)


@app.command()
def progreso() -> None:
    """Muestra tu progreso."""
    profile = state.load_profile()
    if not profile:
        console.print("[dim]Aún no te registraste. Corre `matcom-gym` para empezar.[/]")
        return
    exs = catalog.all_exercises()
    done = sum(1 for e in exs if state.exercise_status(e.slug) == "done")
    in_prog = sum(1 for e in exs if state.exercise_status(e.slug) == "in_progress")
    console.print(f"[bold]{profile['name']}[/] ({profile['group']})")
    console.print(f"Resueltos: [green]{done}[/] / {len(exs)}")
    if in_prog:
        console.print(f"En progreso: [yellow]{in_prog}[/]")


@app.command()
def hola(nombre: str = "estudiante") -> None:
    """Smoke test."""
    console.print(f"[green]Hola, {nombre}![/] Bienvenido a matcom-gym.")


if __name__ == "__main__":
    app()
