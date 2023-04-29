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

### others refs
- https://flask.palletsprojects.com/en/latest/testing/
- https://hub.docker.com/_/microsoft-mssql-server