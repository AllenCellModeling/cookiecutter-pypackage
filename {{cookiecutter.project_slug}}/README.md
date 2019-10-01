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
**Stable Release:** `pip install aicsimageio`<br>
**Development Head:** `pip install git+https://github.com/AllenCellModeling/aicsimageio.git`

## Development
See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

{% if is_open_source %}
***Free software: {{ cookiecutter.open_source_license }}***
{% endif %}
