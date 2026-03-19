from typing import Optional

import typer

from plaster.commands.echo import echo

app = typer.Typer(
    name="plaster",
    no_args_is_help=True,
    rich_markup_mode="rich",
    help="CLI wallpaper management",
)


def version_callback(value: bool) -> None:
    if value:
        typer.echo("plaster 0.1.0")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None, "--version", "-v", callback=version_callback, is_eager=True,
        help="Show version and exit.",
    ),
) -> None:
    """CLI wallpaper management."""


app.command()(echo)


if __name__ == "__main__":
    app()
