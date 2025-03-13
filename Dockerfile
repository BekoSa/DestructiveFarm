FROM python:3.11-slim

WORKDIR /app

COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV FLAGS_DATABASE=/var/destructivefarm/flags.sqlite
ENV FLASK_APP=/app/server/standalone.py

COPY server ./server

VOLUME [ "/var/destructivefarm" ]
EXPOSE 5000

ENTRYPOINT "./server/start_server.sh"