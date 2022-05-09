FROM python:3.9.9-bullseye

ARG APP_DIR=/var/controller/cm-daemon
WORKDIR $APP_DIR

RUN pip install psycopg2

ADD requirements.txt $APP_DIR
RUN pip install -r requirements.txt
