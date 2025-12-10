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

## Run with Docker Compose

First run:
```bash
docker-compose run --rm flaskr sh -c "flask --app flaskr init-db"
docker-compose up --build
```
Subsequent runs:
```bash
docker-compose up
```