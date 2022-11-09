import nox


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def tests(session):
    session.install("pip", "install", ".")
    session.install("pip", "install", ".[test]")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("pip", "install", ".[dev]")
    session.run("isort", ".")
    session.run("black", ".")
    session.run("flake8", ".")
    session.run("mypy", "src")
