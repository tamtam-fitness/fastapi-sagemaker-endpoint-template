#!/bin/bash
docker build -t test-endpoint .
docker run -p 8080:8080 -e ENV=local --rm test-endpoint serve