#RESTORE
gunzip < $1 | docker exec -i nguserxp_db_1 psql -U postgres
