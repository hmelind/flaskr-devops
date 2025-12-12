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
docker-compose run --rm web flask --app flaskr init-db
docker-compose up 
```
Subsequent runs:
```bash
docker-compose up
```

## Jenkins Setup

```bash
docker run -it --rm -p 8080:8080 -p 50000:50000 -v .\jenkins_home:/var/jenkins_home -v //var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
```
