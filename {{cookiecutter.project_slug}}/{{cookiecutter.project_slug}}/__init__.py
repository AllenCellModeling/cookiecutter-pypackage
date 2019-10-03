# -*- coding: utf-8 -*-

"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = "{{ cookiecutter.full_name }}"
__email__ = "{{ cookiecutter.email }}"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "{{ cookiecutter.version }}"


def get_module_version():
    return __version__


from .example import Example  # noqa: F401
