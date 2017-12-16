#!/usr/bin/env bash

if [[ $EUID > 0 ]] ; then
            echo "You need root privileges for this script."
            exit 1
fi

rm /usr/bin/lk
rm /usr/share/lib.py
rm ~/.lk
rm /etc/latest_kernel