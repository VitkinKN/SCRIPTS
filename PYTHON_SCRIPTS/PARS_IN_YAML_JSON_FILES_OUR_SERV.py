import socket
import time
import os
import json
import yaml
numer = 1 
regal = {'github.com': '', 'mail.google.com': ' ', 'google.com': ' '}
if not os.path.isfile('pars.json'):
    serv_json = open("pars.json", "w+")
if not os.path.isfile('pars.yaml'):
    serv_yaml = open("pars.yaml", "w+") 
while numer == 1:
    for server in regal:
        ip_server = socket.gethostbyname(server)
        if ip_server in regal[server]:
            print(server + ' - ' + ip_server)
            del regal[server]
            regal[server] =  ip_server
        else:
            print('ERROR ' +  server + ' IP mismatch: ' + regal[server] +' ' + ip_server)
            del regal[server]
            regal[server] =  ip_server
            with open('pars.json', 'w') as outfile:
                for server in regal:
                    json.dump({server : regal[server]}, outfile)
            with open('pars.yaml', 'w') as outfile1:
                yaml.dump(regal, outfile1, default_flow_style=False)
    time.sleep(1)
