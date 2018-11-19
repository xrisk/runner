#!/usr/bin/env bash
set -e 

apk update && \
    apk add python3 nodejs g++ bash firejail
mkdir -p /sandbox
chown vagrant:vagrant /sandbox
cd /app
pip3 install -r requirements.txt