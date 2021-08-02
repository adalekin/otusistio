FROM python:3.6-alpine3.7 as base
FROM base as builder

RUN mkdir /install
WORKDIR /install

# Install dependencies
RUN apk add --no-cache  \
        gcc \
        libc-dev \
        libffi-dev \
        linux-headers \
        openssl-dev

RUN pip install --upgrade pip

COPY requirements.txt /tmp/

RUN pip wheel --wheel-dir=/tmp/wheelhouse -r /tmp/requirements.txt
RUN pip install --prefix=/install -r /tmp/requirements.txt --no-index --find-links=/tmp/wheelhouse --no-warn-script-location

FROM base

# Install dependencies
RUN apk add --no-cache \
        bash \
        libssl1.0 \
        netcat-openbsd

COPY --from=builder /install /usr/local
COPY . /code/

WORKDIR /code/

CMD ["gunicorn", "deeplinks.main:app", "-b", ":8000", "--worker-class", "aiohttp.GunicornWebWorker"]
