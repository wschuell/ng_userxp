FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install --yes --force-yes apt-utils build-essential python-dev liblzo2-dev liblzma-dev libsqlite3-dev python-tk tmux
RUN pip install numpy matplotlib scipy django-dbbackup psycopg2 codecov coverage
ADD requirements-prod.txt /
RUN pip install -r requirements-prod.txt
ENV PGDATA /postgresql-data
ADD init_db.sh /
RUN bash init_db.sh
RUN mkdir /code
WORKDIR /code
