#!/bin/bash

bash backup_sql.sh &&
docker exec -it ng /code/update.sh $1
