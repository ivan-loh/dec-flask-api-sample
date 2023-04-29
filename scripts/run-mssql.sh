#!/bin/bash

docker pull mcr.microsoft.com/mssql/server:2019-latest

docker run -d \
    --name mssql-server \
    -e "ACCEPT_EULA=Y" \
    -e "MSSQL_SA_PASSWORD=devDBpassword!@#$" \
    -p 1433:1433 \
    -d mcr.microsoft.com/mssql/server:2019-latest

# If we need to access it, replace the container_id
#docker exec -it <container_id|container_name> \
#    /opt/mssql-tools/bin/sqlcmd \
#    -S localhost \
#    -U sa -P devDBpassword!@#$
