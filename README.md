# Cookiecutter PyPackage

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

AICS Cookiecutter template for a Python package.

## Features
* Local testing uses `tox` and `pytest` for local testing, simply run `tox` or `make build` from a terminal in the
project home directory
* Builds and runs unit tests on Windows, Mac, and Ubuntu on every branch and pull request commit using GitHub Actions
* Releases your Python Package to PyPI when you push to `stable` using GitHub Actions
* Pre-configured to work with Sphinx and readthedocs doc generation
* Example code samples for objects, tests, and bin scripts

## The Four Commands You Need To Know
1. `pip install -e .[dev]`

    This will install your package in editable mode with all the required development dependencies (i.e. `tox`).

2. `make build`

    This will run `tox` which will run all your tests in both Python 3.6 and Python 3.7 as well as linting your code.

3. `make clean`

    This will clean up various Python and build generated files so that you can ensure that you are working in a clean
    environment.

4. `make docs`

    This will generate and launch a web browser to view the most up-to-date documentation for your Python package.

## Quickstart
To use this template use the following commands and then follow the prompts from the terminal.

1. `pip install cookiecutter`
2. `cookiecutter gh:AllenCellModeling/cookiecutter-pypackage`

#### Optional Steps:
* Register your project with Codecov:
  * Make an account on [codecov.io](https://codecov.io) (Recommended to sign in with GitHub)
  * Select the organization you want to link a repository to and click: `Add new repository`
  * Copy the token provided, go to your GitHub repository's settings and under the `Secrets` tab, add a secret called
  `CODECOV_TOKEN` with the token you just copied. Don't worry, no one will see this token because it will be encrypted.
* Register your project with PyPI:
  * Make an account on [pypi.org](https://pypi.org)
  * Go to your GitHub repository's settings and under the `Secrets` tab, add a secret called `PYPI_TOKEN` with your
  password for your PyPI account. Don't worry, no one will see this password because it will be encrypted.
  * Next time you push to the branch: `stable`, GitHub actions will build and deploy your Python package to PyPI.
  * _Recommendation: Prior to pushing to `stable` it is recommended to install and run `bumpversion` as this will,
  tag a git commit for release and update the `setup.py` version number._
* Add branch protections to `master` and `stable`
  * To protect from just anyone pushing to `master` or `stable` (the branches with more tests and deploy configurations)
  * Go to your GitHub repository's settings and under the `Branches` tab, click `Add rule` and select the settings you
  believe best.
  * _Recommendations:_
    * _Require pull request reviews before merging_
    * _Require status checks to pass before merging (All, as administrator of the repo you can override)_
    * _Include administrators_
    * _Restrict who can push to matching branches_
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.


## Suggested Git Branch Strategy
1. `master` is for the most up-to-date development, very rarely should you directly commit to this branch. GitHub
Actions will run on every push and on a CRON to this branch but still recommended to commit to your development
branches and make pull requests to master.
2. `stable` is for releases only. When you want to release your project on PyPI, simply make a PR from `master` to
`stable`, this template will handle the rest as long as you have added your PyPI information described in the above
**Optional Steps** section.
3. Your day-to-day work should exist on branches separate from `master`. Even if it is just yourself working on the
repository, make a PR from your working branch to `master` so that you can ensure your commits don't break the
development head. GitHub Actions will run on every push to any branch or any pull request from any branch to any other
branch.


**Original repo:** https://github.com/audreyr/cookiecutter-pypackage/
