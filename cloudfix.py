#!/usr/bin/env python
import yaml

with open("/etc/netplan/50-cloud-init.yaml", "r") as f:
  config = yaml.safe_load(f)

config['network']['renderer'] = "networkd"
config['network']['ethernets']['eth0']['dhcp4'] = 'no'
config['network']['ethernets']['eth0']['dhcp6'] = 'no'

route_to = config['network']['ethernets']['eth0']['gateway4']
route_to += '/32'

config['network']['ethernets']['eth0']['routes']['to'] = route_to
config['network']['ethernets']['eth0']['routes']['via'] = "0.0.0.0"
config['network']['ethernets']['eth0']['routes']['scope'] = "link"

with open("/etc/netplan/51-cloud-init.yaml", "w") as fp:
  yaml.dump(config, fp)
