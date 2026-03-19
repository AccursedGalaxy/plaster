import typer

app = typer.Typer()


@app.command()
def main():
    pass


@app.command()
def fetch():
    pass


if __name__ == "__main__":
    app()
