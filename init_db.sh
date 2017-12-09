#!/bin/bash
if [ ! -x init_db_done ]
then






NEWDIR=/postgresql-data
test -d $NEWDIR || mkdir -p $NEWDIR
chmod 777 $NEWDIR
#ORIG_CONF=$(find /etc/postgresql/*/main/postgresql.conf)
#OLD_CONF=$ORIG_CONF.old
#mv $ORIG_CONF $OLD_CONF
#cat $OLD_CONF | sed -e "s|data_directory = |data_directory = '$NEWDIR'     #|" > $ORIG_CONF
#initdb -D $NEWDIR

#service postgresql initdb -E 'UTF8' --pgdata=$NEWDIR
#export PGDATA=$NEWDIR
apt-get install --yes --force-yes postgresql postgresql-contrib libpq-dev
ORIG_DIR=$(find /etc/postgresql/*/main)
chown -R postgres.postgres $NEWDIR
chmod 700 $NEWDIR
service postgresql start

su - postgres << 'EOF'
createdb ng_userxp
psql -c "CREATE USER ng_userxp_user WITH PASSWORD 'pass';"
createdb naminggames
psql -c "CREATE USER naminggames WITH PASSWORD 'naminggames';"
psql -c "ALTER USER ng_userxp_user CREATEDB;"
EOF

DJANGO_MODULE_SETTINGS="main_site.production_settings"
export DJANGO_MODULE_SETTINGS
python manage.py makemigrations ng
python manage.py migrate
python manage.py collectstatic --noinput

touch init_db_done


fi
