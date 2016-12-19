#!/bin/bash

# Nginx install script used into scaleway.c1 servers dure to ARM architecture

NGINX_VERSION="1.11.7"

# As root
cd

# Install nginx requirements
yum install -y pcre-devel zlib-devel

# Download nginx package
curl -O http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz
tar xf nginx-$NGINX_VERSION.tar.gz
cd nginx-$NGINX_VERSION

# Configure, make and Install
./configure
make
make install

# Symlink binary
ln -s /usr/local/nginx/sbin/nginx /usr/sbin/nginx

# Now create the service file as in the template in
# /etc/systemd/system/nginx.service

# Uncomment the pid directive from the nginx conf and change its value to
# /run/nginx.pid

# add rule to iptables
# -A IN_public_allow -p tcp -m tcp --dport 80 -m conntrack --ctstate NEW -j ACCEPT
