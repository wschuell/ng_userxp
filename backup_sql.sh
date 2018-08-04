#!/bin/bash

docker exec --user postgres -t ng pg_dumpall -c | gzip > ./backup_postgres/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql.gz
