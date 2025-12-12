FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip \
	&& pip install --no-cache-dir pytest \
	&& pip install --no-cache-dir -e .

ENV PYTHONPATH=/app

EXPOSE 5000

CMD ["flask", "--app", "flaskr:create_app", "run", "--host=0.0.0.0"]
