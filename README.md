# install Poetry

curl -sSL https://install.python-poetry.org | python3 -

~/.local/bin/poetry --version

export PATH="$HOME/.local/bin:$PATH"

poetry --version

# create poetry environment

poetry install --no-root

poetry show

poetry run python test.py