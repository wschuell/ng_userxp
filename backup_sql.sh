#!/bin/bash
mkdir -p backup_postgres
GITCOMMIT=$(git rev-parse --verify HEAD --short)
docker exec --user postgres -t nguserxp_db_1 pg_dumpall -a | gzip > ./backup_postgres/dump_`date +%Y-%m-%d"_"%H_%M_%S`_"$GITCOMMIT".sql.gz


