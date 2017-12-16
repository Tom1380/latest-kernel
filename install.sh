#!/usr/bin/env bash

if [[ $EUID > 0 ]] ; then
            echo "You need root privileges for this script."
            exit 1
fi

cp lk /usr/bin/lk
cp lib.py /usr/share/lib.py
cp configuration_file ~/.lk
touch /etc/latest_kernel