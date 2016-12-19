#!/bin/bash

# Emacs install script used into scaleway.c1 servers due to ARM arch

EMACS_VERSION="25.1"


# Asume root
cd

# Install dependencies
yum install -y ncurses.devel

# Download package
curl -O http://ftp.rediris.es/mirror/GNU/gnu/emacs/emacs-$EMACS_VERSION.tar.xz

# Configure, Make, and Install
./configure
make
make install
