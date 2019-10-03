{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/workflows/Build%20Master/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/actions)
[![Code Coverage](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

{{ cookiecutter.project_short_description }}

---

## Features
* Store values and retain the prior value in memory
* ... some other functionality

## Quick Start
```python
from {{ cookiecutter.project_slug }} import Example

a = Example()
a.get_value()  # 10
```

## Installation
**Stable Release:** `pip install {{ cookiecutter.project_slug }}`<br>
**Development Head:** `pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git`

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

#### The Three Commands You Need To Know
1. `make build`

    This will run `tox` which will run all your tests in both Python 3.6 and Python 3.7 and it will lint your code.

2. `make clean`

    This will clean up various Python and build generated files so that you can ensure that you are working in a clean
    environment.

3. `make docs`

    This will generate and launch a web browser to view the most up-to-date documentation for your Python package.

#### Suggested Git Branch Strategy
1. `master` is for the most up-to-date development, very rarely should you directly commit to this branch.
2. `stable` is for releases only. When you want to release your project on PyPI, simple make a PR from `master` to
`stable`, this template will handle the rest.
3. Your day to day work should exist on branches separate from `master`. Even if it is just yourself working on the
repository, make a PR from your working branch to `master` so that you get GitHub actions to run tests, linting, and
code coverage checks.

#### Additional Optional Setup Steps:
* Register {{ cookiecutter.project_slug }} with Codecov:
  * Make an account on [codecov.io](https://codecov.io) (Recommended to sign in with GitHub)
  * Select `{{ cookiecutter.github_username }}` and click: `Add new repository`
  * Copy the token provided, go to your [GitHub repository's settings and under the `Secrets` tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets), add a secret called
  `CODECOV_TOKEN` with the token you just copied. Don't worry, no one will see this token because it will be encrypted.
* Register your project with PyPI:
  * Make an account on [pypi.org](https://pypi.org)
  * Go to your [GitHub repository's settings and under the `Secrets` tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/secrets),
  add a secret called `PYPI_TOKEN` with your
  password for your PyPI account. Don't worry, no one will see this password because it will be encrypted.
  * Next time you push to the branch: `stable`, GitHub actions will build and deploy your Python package to PyPI.
  * _Recommendation: Prior to pushing to `stable` it is recommended to install and run `bumpversion` as this will,
  tag a git commit for release and update the `setup.py` version number._
* Add branch protections to `master` and `stable`
    * To protect from just anyone pushing to `master` or `stable` (the branches with more tests and deploy
    configurations)
    * Go to your [GitHub repository's settings and under the `Branches` tab](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/settings/branches), click `Add rule` and select the
    settings you believe best.
    * _Recommendations:_
      * _Require pull request reviews before merging_
      * _Require status checks to pass before merging (Select all, as administrator of the repo you can override)_
      * _Include administrators_
      * _Restrict who can push to matching branches_
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.

{% if is_open_source %}
***Free software: {{ cookiecutter.open_source_license }}***
{% endif %}
