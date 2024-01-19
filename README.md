# thelab-pre-commit-hooks

## Installation

Sample `.pre-commit-config.yaml`:

```yaml
- repo: https://gitlab.com/thelabnyc/thelab-pre-commit-hooks
  rev: r0.0.1
  hooks:
    - id: update-copyright-year
      args:
        file: LICENSE
        pattern: '\\[?(?P<year>\\d{4})\\]?\\sthelab'
```
