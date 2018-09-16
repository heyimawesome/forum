FROM python:3.7-alpine
#FROM python:3.7-slim

LABEL maintainer="james.heimberger@netlag.xyz"

RUN apk update && apk add libpq postgresql-dev build-base

#RUN apt-get update && apt-get install -qq -y \
#    build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR ${INSTALL_PATH}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "forum:create_app()"



