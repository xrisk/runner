#!/usr/bin/env bash
set -e 

curl -sL https://deb.nodesource.com/setup_11.x | bash -
curl -qO https://excellmedia.dl.sourceforge.net/project/firejail/firejail/firejail_0.9.56_1_amd64.deb

apt-get update && \
    apt-get install -y python3.6 python3-pip nodejs nodejs

dpkg -i firejail_0.9.56_1_amd64.deb

apt-get install -f 

mkdir -p /sandbox
cd /vagrant
pip3 install --no-cache-dir -r requirements.txt