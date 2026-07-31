#!/bin/bash
#Displays all HTTP methods a server will accept for a given URL
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | sed 's/Allow: //I' | tr -d '\r'
