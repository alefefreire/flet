# Password Generator

This is a project for a password generator built with [Flet](https://flet.dev/). The generator creates passwords that can include numbers, symbols, uppercase, and lowercase letters. The user can choose the number of characters for the password, up to a maximum of 20.

## Features

- Secure password generation with numbers, symbols, uppercase, and lowercase letters.
- Option to choose the number of characters, up to a limit of 20.
- Interactive graphical interface built with Flet.

## Installation

To set up the project environment, follow the steps below:

1. Install [pyenv](https://github.com/pyenv/pyenv) to manage Python versions:
   ```bash
   curl https://pyenv.run | bash

2. Add the following lines to your `~/.bashrc` or `~/.zshrc`:
    ```bash
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    ```
3. Install Python version 3.12:
    ```bash
    pyenv install 3.12.0
    pyenv local 3.12.0
    ```
4. Install [Poetry](https://python-poetry.org/) for dependency management:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
5. Install the project dependencies:
    ```bash
    poetry install
    ```

## Tests and Linting
This project uses `tox` to run unit tests and perform static code analysis. To run the tests and linting, simply execute the following command:
    
  ```bash
  poetry run tox
  ```

## Technologies Used
- Python 3.12
- Flet
- Poetry
- Tox

## Running the App Locally
Run the app with the following command:
```bash
cd src
flet run app.py
````



