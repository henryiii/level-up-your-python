import nox
from pathlib import Path

nox.needs_version = ">=2022.1.7"
DIR = Path(__file__).parent.resolve()


@nox.session(reuse_venv=True)
def pyodide(session: nox.Session) -> None:
    session.install("jupyterlite[lab]")
    session.run("jupyter", "lite", "init")
    session.run("jupyter", "lite", "build", "--contents=notebooks")
    
    avoid_pyodide_bug()

    if "--serve" in session.posargs:
        session.run("jupyter", "lite", "serve")


# Required for JupyterLite 0.1.0b12
def avoid_pyodide_bug():
    output = DIR / "_output"
    build = output / "build"
    paths = [
        output / "jupyterlite.schema.v0.json",
        *build.glob("*.js"),
        *build.glob("*.js.map"),
    ]
    for path in paths:
        txt = path.read_text()
        txt = txt.replace(
            "https://cdn.jsdelivr.net/pyodide/v0.21.0",
            "https://cdn.jsdelivr.net/pyodide/v0.21.3",
        )
        path.write_text(txt)
