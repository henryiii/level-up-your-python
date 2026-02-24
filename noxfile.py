import nox

nox.needs_version = ">=2022.1.7"


@nox.session(reuse_venv=True)
def pyodide(session: nox.Session) -> None:
    session.install(
        "jupyterlite-core~=0.7.2",
        "jupyterlab~=4.5.5",
        "notebook~=7.5.4",
        "jupyterlite-pyodide-kernel~=0.7.0",
    )
    session.run("jupyter", "lite", "init")
    session.run("jupyter", "lite", "build", "--contents=notebooks")

    if session.interactive:
        session.run("jupyter", "lite", "serve")
