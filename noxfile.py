import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session(venv_backend="virtualenv", python="3.11")
def doc(session):
    session.install("-r", "requirements.txt")
    session.run("sphinx-build", "doc", "site")