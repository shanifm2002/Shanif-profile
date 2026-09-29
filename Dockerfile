FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir Flask gunicorn

COPY . .

EXPOSE 5000

CMD ["python", "-m", "gunicorn", "-b", "0.0.0.0:5000", "-w", "2", "app:app"]