FROM python:3.11-slim

WORKDIR /app

COPY ./server ./server
RUN pip install --no-cache-dir -r ./server/requirements.txt

ENV FLAGS_DATABASE=/var/destructivefarm/flags.sqlite
ENV FLASK_APP=/app/server/standalone.py



VOLUME [ "/var/destructivefarm" ]
EXPOSE 5000

ENTRYPOINT ["sh", "./server/start_server.sh"]