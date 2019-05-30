{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}
        :alt: Release Status

.. image:: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?branch=master
        :target: https://travis-ci.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Build Status

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest
        :alt: Documentation Status

.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/branch/master/graph/badge.svg
        :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Codecov Status
{%- endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
{% endif %}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.


Features
--------

* TODO

Support
-------
We are not currently supporting this code, but simply releasing it to the community AS IS but are not able to provide any guarantees of support. The community is welcome to submit issues, but you should not expect an active response.

Credits
-------

This package was created with Cookiecutter_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
