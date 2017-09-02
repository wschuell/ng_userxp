#!/bin/bash
set -e
LOGFILE=./log/gunicorn/ng_userxp.log
LOGDIR=$(dirname $LOGFILE)
LOGLEVEL=info   # info ou warning une fois l'installation OK
NUM_WORKERS=3    # Règle : (2 x $num_cores) + 1
DJANGO_SETTINGS_MODULE="main_site.production_settings"
export DJANGO_SETTINGS_MODULE

echo $DJANGO_SETTINGS_MODULE

# user/group to run as
USER=root
GROUP=root

# source ../bin/activate  # Cette ligne ne sert que si vous utilisez virtualenv
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=$LOGLEVEL \
  --log-file=$LOGFILE 2>>$LOGFILE -b 127.0.0.1:8000 \
  main_site.wsgi:application
