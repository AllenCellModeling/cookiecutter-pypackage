# Cookiecutter PyPackage

[![Example Repo Status](https://github.com/AllenCellModeling/cookiecutter-pypackage/workflows/Build%20Example%20Repo/badge.svg)](https://github.com/AllenCellModeling/cookiecutter-pypackage/tree/example-build)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

AICS Cookiecutter template for a Python package.

## About

`Cookiecutter` is a Python package to generate templated projects.
This repository is a template for `cookiecutter` to generate a Python project which
contains following:

-   A directory structure for your project
-   Prebuilt `setup.py` file to help you develop and install your package
-   Includes examples of good Python practices, including tests
-   Continuous integration
    -   Preconfigured to generate project documentation
    -   Preconfigured to automatically run tests every time you push to GitHub
    -   Preconfigured to help you release your package publicly (PyPI)

We think that this template provides a good starting point for any Python project.

## Features

-   Uses `tox` (an environment manager) and `pytest` for local testing, simply run `tox`
    or `make build` from a terminal in the project home directory
-   Runs tests on Windows, Mac, and Ubuntu on every branch and pull request commit using
    GitHub Actions
-   Releases your Python Package to PyPI when you push to `main` after using
    `bump2version`
-   Automatically builds documentation using Sphinx on every push to main and deploys
    to GitHub Pages
-   Includes example code samples for objects, tests, and bin scripts

## Example

-   For an example of the base project that is built from this template, go to the
    [example-build branch](https://github.com/AllenCellModeling/cookiecutter-pypackage/tree/example-build).

## Quickstart

To use this template use the following commands and then follow the prompts from the
terminal.

1. `pip install cookiecutter`
2. `cookiecutter gh:AllenCellModeling/cookiecutter-pypackage`

## The Four Commands You Need To Know

1. `pip install -e .[dev]`

    This will install your package in editable mode with all the required development
    dependencies (i.e. `tox`).

2. `make build`

    This will run `tox` which will run all your tests in both Python 3.7
    and Python 3.8 as well as linting your code.

3. `make clean`

    This will clean up various Python and build generated files so that you can ensure
    that you are working in a clean environment.

4. `make docs`

    This will generate and launch a web browser to view the most up-to-date
    documentation for your Python package.

#### Optional Steps:

-   Turn your project into a GitHub repository:
    -   Make an account on [github.com](https://github.com)
    -   Go to [make a new repository](https://github.com/new)
    -   _Recommendations:_
        -   _It is strongly recommended to make the repository name the same as the Python
            package name_
        -   _A lot of the following optional steps are *free* if the repository is Public,
            plus open source is cool_
    -   After a GitHub repo has been created, run the commands listed under:
        "...or push an existing repository from the command line"
-   Register your project with Codecov:
    -   Make an account on [codecov.io](https://codecov.io)(Recommended to sign in with GitHub)
        everything else will be handled for you.
-   Ensure that you have set GitHub pages to build the `gh-pages` branch by selecting the
    `gh-pages` branch in the dropdown in the "GitHub Pages" section of the repository settings.
-   Register your project with PyPI:
    -   Make an account on [pypi.org](https://pypi.org)
    -   Go to your GitHub repository's settings and under the `Secrets` tab, add a secret
        called `PYPI_TOKEN` with your password for your PyPI account. Don't worry, no one
        will see this password because it will be encrypted.
    -   Next time you push to the branch: `main` after using `bump2version`, GitHub
        actions will build and deploy your Python package to PyPI.

#### Suggested Git Branch Strategy

1. `main` is for the most up-to-date development, very rarely should you directly
   commit to this branch. GitHub Actions will run on every push and on a CRON to this
   branch but still recommended to commit to your development branches and make pull
   requests to main. If you push a tagged commit with bumpversion, this will also release to PyPI.
2. Your day-to-day work should exist on branches separate from `main`. Even if it is
   just yourself working on the repository, make a PR from your working branch to `main`
   so that you can ensure your commits don't break the development head. GitHub Actions
   will run on every push to any branch or any pull request from any branch to any other
   branch.
3. It is recommended to use "Squash and Merge" commits when committing PR's. It makes
   each set of changes to `main` atomic and as a side effect naturally encourages small
   well defined PR's.

**Original repo:** https://github.com/audreyr/cookiecutter-pypackage/
