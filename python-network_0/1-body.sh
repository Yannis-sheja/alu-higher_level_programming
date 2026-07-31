#!/bin/bash
# Sends a GET request to a URL, follows redirects, and displays the body only if the final status code is 200
curl -s -L -o /tmp/1-body_output -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/1-body_output
