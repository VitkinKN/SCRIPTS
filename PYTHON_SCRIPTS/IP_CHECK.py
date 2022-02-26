import socket
import time
numer = 1 
regal = {'drive.google.com': '', 'mail.google.com': ' ', 'google.com': ' '}
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
    time.sleep(1)
# This program checks google services, returns their ip and displays a message in the terminal about the service matching - address. Throws an error if it doesn't match.