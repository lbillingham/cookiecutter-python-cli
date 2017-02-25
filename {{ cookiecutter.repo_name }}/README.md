# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}


# Installation

Simply run:

    $ pip install .


# Usage

To use it:

    $ {{ cookiecutter.script_name }} --help

# Development

Install the test/development dependencies

    $ pip install -r requirements_dev.txt

Run the tests and get a coverage report

    $ pytest --cov-report term-missing --cov {{ cookiecutter.package_name }}
