FROM python:3.10.11-alpine3.18

ENV PYTHONUNBUFFERED=1

RUN apk update --no-cache && apk add --no-cache  \
    build-base \
    libpq-dev

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

COPY ./.env* /.env
COPY ./compose/set_env /set_env
RUN chmod +x /set_env
COPY ./compose/django/start /start
RUN chmod +x /start
COPY ./compose/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]
CMD ["/start"]
