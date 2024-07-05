#!/bin/bash
# Sends a request to that URL using cURL, and displays the size of the response body in bytes.
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
