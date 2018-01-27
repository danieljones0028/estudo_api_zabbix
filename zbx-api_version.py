#!/home/daniel/anaconda3/envs/vmpy35/bin/python

from pyzabbix import ZabbixAPI
import sys
import logging
stream = logging.StreamHandler(sys.stdout)
stream.setLevel(logging.DEBUG)
log = logging.getLogger('pyzabbix')
log.addHandler(stream)
log.setLevel(logging.DEBUG)


# Login (in case of HTTP Auth, only the username is needed, the password, if passed, will be ignored)
zapi = ZabbixAPI("http://172.16.241.102/zabbix")
zapi.login("Admin", "zabbix")

# Enable HTTP auth
zapi.session.auth = ("Admin", "zabbix")

# Disable SSL certificate verification
zapi.session.verify = False

# Specify a timeout (in seconds)
zapi.timeout = 5.1

print("Connected to Zabbix API Version %s" % zapi.api_version())
