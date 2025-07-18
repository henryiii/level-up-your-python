import nox

nox.needs_version = ">=2022.1.7"


@nox.session(reuse_venv=True)
def pyodide(session: nox.Session) -> None:
    session.install(
        "jupyterlite-core~=0.6.2",
        "jupyterlab~=4.4.3",
        "notebook~=7.4.3",
        "jupyterlite-pyodide-kernel~=0.6.1",
    )
    session.run("jupyter", "lite", "init")
    session.run("jupyter", "lite", "build", "--contents=content")

    if session.interactive:
        session.run("jupyter", "lite", "serve")

