# Sample Project setup
A starter project that uses github-actions to run pytest, flake8, mypy and coverage.

Also with a very pedantic pre-commit to force you to write moderately readable code.

![Tests](https://github.com/violet-fresh4cast/github-actions-tests/actions/workflows/tests.yml/badge.svg)

Run pytest with:
```
pytest --cov=src
```

Run flake8 with:
```
flake8
```

Run mypy with:
```
mypy src
```
