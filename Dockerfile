FROM python:3.12-slim

WORKDIR /app

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["flask", "--app", "flaskr", "run", "--host=0.0.0.0"]
