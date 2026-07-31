#!/bin/bash
# Sends a GET request with a custom header and displays the body of the response
curl -v -H "X-HolbertonSchool-User-Id: 98" "$1"
