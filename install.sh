#!/bin/bash

cwd=$(pwd)
export PATH=$(pwd) >> temp.txt

sudo mv /home/saint-rivers/snote/snote.sh /usr/local/bin/snote
sudo chown root: /usr/local/bin/snote
sudo chmod 755 /usr/local/bin/snotes
