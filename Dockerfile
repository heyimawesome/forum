#FROM python:3.7-alpine
FROM python:3.7-slim

LABEL maintainer="james.heimberger@netlag.xyz"

ENV INSTALL_PATH /app
RUN mkdir -p $INSTALL_PATH

WORKDIR ${INSTALL_PATH}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "app.app:create_app()"



