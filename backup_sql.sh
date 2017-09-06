#!/bin/bash

docker exec --user postgres -t ng pg_dumpall | gzip > /data/backup_postgres/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz