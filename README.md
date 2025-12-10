## Run locally

```bash
flask --app flaskr init-db
flask --app flaskr run
```

## Run with Docker

```bash
docker build -t flaskr-demo .
docker run -p 5000:5000 flaskr-demo
```
