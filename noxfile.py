import nox


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def tests(session):
    session.install("pytest")
    session.install("pytest-cov")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("isort")
    session.run("isort", ".")
    session.install("black")
    session.run("black", ".")
    session.install("flake8")
    session.run("flake8", ".")


@nox.session
def typing(session):
    session.install("mypy")
    session.run("mypy", "src")
