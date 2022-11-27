import nox


@nox.session(python=["3.7", "3.8", "3.9", "3.10", "3.11"])
def tests(session):
    session.install("pip-tools")
    session.run(
        "python",
        "-m",
        "piptools",
        "sync",
        "--quiet",
        "requirements.txt",
        "dev-requirements.txt",
    )
    session.run("python", "-m", "pytest")


@nox.session
def lint(session):
    session.install("pip-tools")
    session.run(
        "python",
        "-m",
        "piptools",
        "sync",
        "--quiet",
        "requirements.txt",
        "dev-requirements.txt",
    )
    session.run("pyupgrade")
    session.run("isort", ".")
    session.run("black", ".")
    session.run("flake8", ".")
    session.run("mypy", "src")
