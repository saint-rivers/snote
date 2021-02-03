#!/bin/bash

cwd=$(pwd)
#export PATH=$PATH:$(pwd)+somethingelse

sudo rm /usr/local/bin/snote
sudo cp $cwd/snote.sh /usr/local/bin/snote
sudo chown root: /usr/local/bin/snote
sudo chmod 755 /usr/local/bin/snote
