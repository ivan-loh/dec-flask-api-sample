#!/bin/bash

docker exec \
    -it mssql-server /opt/mssql-tools/bin/sqlcmd -S localhost \
    -U sa \
    -P 'devDBpassword!@#$' -Q 'CREATE DATABASE devdb;'