build

```commandline
docker build -t flask-api-example .
```
run

```commandline
docker run -p 5000:5000 flask-api-example
```

testing
```
PYTHONPATH=. pytest
```

folder structure
```commandline
git ls-tree -r --name-only HEAD | tree --fromfile
```

linting with flake8
```commandline
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

### others refs
- https://flask.palletsprojects.com/en/latest/testing/
- https://hub.docker.com/_/microsoft-mssql-server