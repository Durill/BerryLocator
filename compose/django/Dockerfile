FROM python:3.10.11-alpine3.18

ENV PYTHONUNBUFFERED=1

RUN apk update --no-cache && apk add --no-cache  \
    build-base \
    libpq-dev

# install those 2 packages (build-base, libxslt-dev) using Alpine package manager 'apk'
# Using Alpine Linux package manager because Docker containers relies on this
# lightweight distro
RUN apk --update add build-base libxslt-dev

# add packages (gcc, libc-dev, geos-dev, geos) to virtual package group '.build-deps'
# from 'runDeps=...' scanning files in '/usr/local' to determine runtime dependencies
# 'runDeps' and add them to virtual package group '.rundeps'
RUN apk add --virtual .build-deps \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        gcc libc-dev geos-dev geos gdal-dev && \
    runDeps="$(scanelf --needed --nobanner --recursive /usr/local \
    | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
    | xargs -r apk info --installed \
    | sort -u)" && \
    apk add --virtual .rundeps $runDeps

# return information about installed GEOS libraries and binaries (geos-config)
# and printing compiler flags that are necessary to compile a plug-in (--cflags)
RUN geos-config --cflags

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# delete packages (build-base, python3-dev) to remove temp build dependencies
# removes package cache to reduce size of the Docker image
RUN apk del build-base python3-dev && \
    rm -rf /var/cache/apk/*

COPY ./.env* /.env
COPY ./compose/set_env /set_env
RUN chmod +x /set_env
COPY ./compose/django/start /start
RUN chmod +x /start
COPY ./compose/django/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]
CMD ["/start"]
