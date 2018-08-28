#!/bin/bash
set -e
LOGFILE=./logs/gunicorn/ng_userxp.log
LOGDIR=$(dirname $LOGFILE)
LOGLEVEL=info
NUM_WORKERS=$(($(nproc --all) * 2 + 1))
DJANGO_SETTINGS_MODULE="main_site.production_settings"
export DJANGO_SETTINGS_MODULE

# user/group to run as
USER=root
GROUP=root

# source ../bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=$LOGLEVEL \
  -b 0.0.0.0:8000 --reload \
  main_site.wsgi:application
# --log-file=$LOGFILE 2>>$LOGFILE
