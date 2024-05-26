FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
