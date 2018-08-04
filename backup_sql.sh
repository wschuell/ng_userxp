#!/bin/bash
mkdir -p backup_postgres
docker exec --user postgres -t nguserxp_db_1 pg_dumpall -c | gzip > ./backup_postgres/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz
