FROM python:3.11-alpine3.20

RUN mkdir /app
RUN mkdir /data

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ouauth /app

EXPOSE 9999

CMD ["python", "manage.py", "runserver", "0.0.0.0:9999"]
