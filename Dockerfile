FROM python:2
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements-prod.txt /code/
RUN apt-get update && apt-get install --yes --force-yes apt-utils build-essential python-dev liblzo2-dev liblzma-dev libsqlite3-dev python-tk
RUN pip install numpy matplotlib scipy django-dbbackup psycopg2
RUN pip install -r requirements-prod.txt
RUN pip install git+https://github.com/flowersteam/naminggamesal.git@develop
ADD . /code/
ENV PGDATA /postgresql-data
RUN bash init_db.sh
