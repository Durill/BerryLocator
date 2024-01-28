FROM postgres:16.1-alpine3.18

USER postgres

COPY ./.env* /.env
COPY ./compose/set_env /set_env
COPY ./compose/postgres/entrypoint /entrypoint

ENTRYPOINT ["/entrypoint"]
CMD ["docker-entrypoint.sh", "postgres"]
