# thelab-pre-commit-hooks

## Installation

Sample `.pre-commit-config.yaml`:

```yaml
- repo: https://gitlab.com/thelabnyc/thelab-pre-commit-hooks
  rev: r0.0.2
  hooks:
      - id: update-copyright-year
        args:
            file: LICENSE
            pattern: '\\[?(?P<year>\\d{4})\\]?\\sthelab'
      - id: npm-install
```

## Hooks

### `update-copyright-year`

| Argument          | Default                         | Description                                                                        |
| ----------------- | ------------------------------- | ---------------------------------------------------------------------------------- |
| `-f`, `--file`    | `LICENSE`                       | Path to the license file                                                           |
| `-p`, `--pattern` | `\[?(?P<year>\d{4})\]?\sthelab` | Regex pattern for finding the copyright year. Must contain the named group `year`. |

This hook looks for a copyright year in a license file and updates it to the current year.

### `npm-install`

This hook runs `npm install`. This is useful if subsequent hooks depend on `node_modules` existing. Why would this be the case? One example is if your project uses [@thelabnyc/standards](https://gitlab.com/thelabnyc/standards), and thus has dotfiles (like `.markdownlint.json`) that are actually just symlinks into the `node_modules` directory.
