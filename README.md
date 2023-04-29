build

```commandline
docker build -t flask-api-example .
```
run

```commandline
docker run -p 5000:5000 flask-api-example
```

testing
```PYTHONPATH=. pytest```

others refs
- https://flask.palletsprojects.com/en/latest/testing/
- https://hub.docker.com/_/microsoft-mssql-server