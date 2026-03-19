from typer.testing import CliRunner

from plaster.main import app

runner = CliRunner()


def test_app_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "wallpaper" in result.output.lower()


def test_echo():
    result = runner.invoke(app, ["echo", "hello"])
    assert result.exit_code == 0
    assert "hello" in result.output
