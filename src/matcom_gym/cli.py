"""matcom-gym CLI entry point.

M0: skeleton with hello + version. Real commands land in M1+.
"""

import typer
from rich.console import Console

from matcom_gym import __version__

app = typer.Typer(
    name="matcom-gym",
    help="Coding gym for MatCom students.",
    no_args_is_help=False,
)
console = Console()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Default entry — will open the dashboard once the TUI lands."""
    if ctx.invoked_subcommand is not None:
        return
    console.print("[bold cyan]matcom-gym[/] — dashboard llegará en M4.")
    console.print("Mientras tanto:  [dim]matcom-gym --help[/]")


@app.command()
def version() -> None:
    """Print the installed version."""
    console.print(f"matcom-gym {__version__}")


@app.command()
def hola(nombre: str = "estudiante") -> None:
    """Placeholder command — smoke test that wiring works end-to-end."""
    console.print(f"[green]Hola, {nombre}![/] Bienvenido a matcom-gym.")


if __name__ == "__main__":
    app()
