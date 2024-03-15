FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "--config", "gunicorn_config.py"]
