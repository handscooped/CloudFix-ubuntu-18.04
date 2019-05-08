#!/bin/bash

sudo python3 ~/cloudfix.py
sudo rm -r /etc/netplan/50-cloud-init.yaml

sudo netplan apply

clear
cat << "EOF"
 __  __           _            _    _           _     
|  \/  |         | |          | |  | |         | |    
| \  / | __ _ ___| |_ ___ _ __| |__| | __ _ ___| |__  
| |\/| |/ _` / __| __/ _ \ '__|  __  |/ _` / __| '_ \ 
| |  | | (_| \__ \ ||  __/ |  | |  | | (_| \__ \ | | |
|_|  |_|\__,_|___/\__\___|_|  |_|  |_|\__,_|___/_| |_|
EOF
echo
