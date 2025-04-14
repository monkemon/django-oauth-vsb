FROM python:3.11-alpine3.20 as base

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh



FROM base as debug

ENTRYPOINT ["/usr/local/bin/python"]
CMD ["./manage.py", "runserver", "0.0.0.0:9999"]



FROM base as production

ENTRYPOINT ["/bin/sh"]
CMD ["./entrypoint.sh"]


