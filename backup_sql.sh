#!/bin/bash

docker exec -t ng pg_dumpall -c -U postgres | gzip > /data/backup_postgres/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz