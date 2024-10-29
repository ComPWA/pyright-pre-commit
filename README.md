# Pyright mirror

Mirror of [Pyright](https://github.com/microsoft/pyright) for [pre-commit](https://pre-commit.com), created with [`pre-commit-mirror-maker`](https://github.com/pre-commit/pre-commit-mirror-maker). See [github.com/pre-commit/prettier](https://github.com/pre-commit/prettier) for an example of a pre-commit hook for a Node.js package.

### Using Pyright with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/ComPWA/pyright-pre-commit
  rev: ""
  hooks:
    - id: pyright
```

then run `pre-commit autoupdate`.
