#!/bin/bash

apt update 
apt install -y apache2
apt install -y libapache2-mod-wsgi-py3

source ./deploy/reuse_deploy.sh
