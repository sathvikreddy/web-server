#!/usr/bin/env python
import socket
import re
import os

def substringinstring(x,y):
    if (x in y):
        return False
    else :
        return True
def checkinvalidurl(a):
    p= "!@#$%^&*"
    for i in range(0, len(p)) :
        if (p[i] in a) :
            return(p[i] in a)
            break
configfile= open('ws.conf', 'r')
configfile_list= configfile.readlines()
configfile1= open('ws.conf', 'r')
configfile_string= configfile1.read()
rootdirpath=configfile_list[5]
rootdirpath = re.sub(r'^"|"$', '', rootdirpath)
rootdirpath = rootdirpath.rstrip('\n')
os.chdir(rootdirpath)
host = ''
port = int(configfile_list[2])
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    recd = client.recv(size)
    if recd :
        try :
            
            data = recd.decode("utf-8")
            httpreqst= data.split()[0]
            requestedfile= data.split()[1]
            httpversion= data.split()[2]
            connectiontype= data.split()[6]
            if (httpreqst != 'GET'):
                data= " HTTP/1.1 400 Invalid method \n\n"
                print(data)
                client.send(data.encode("utf-8"))
            elif checkinvalidurl(requestedfile) : 
                data= " HTTP/1.1 400 Invalid URI \n\n"
                print(data)
                client.send(data.encode("utf-8"))
            elif httpversion != 'HTTP/1.1':
                data= " HTTP/1.1 400 Invalid HTTP-version \n\n"
                print(data)
                client.send(data.encode("utf-8"))
            elif requestedfile=='/' :
                requestedfile= 'index.html' 
                file= open(requestedfile, 'rb')
                data= file.read()
                client.send(data)
            
            else:
                fileextnsn= requestedfile.split(".")[1]
                fileextnsn= '.'+str(fileextnsn)
                if substringinstring(fileextnsn, configfile_string):
                    data= " HTTP/1.1 501 Not implemented \n\n"
                    print(data)
                    client.send(data.encode("utf-8"))
                else :
                    try :
                        requestedfile= requestedfile[1:]
                        if requestedfile== 'index.ws' or requestedfile == 'index.htm' :
                            requestedfile= 'index.html'
                        header = "\n HTTP/1.1 200 ok \n\n"
                        file= open(requestedfile, 'rb')
                        data1= file.read()
                        
                    except IOError:
                        data= " HTTP/1.1 404 Not found \n\n"
                        client.send(data.encode("utf-8"))
                    client.send(header.encode("utf-8"))
                    client.send(data1)

        except IOError:
                data= "\n HTTP/1.1 500 Internal server error \n\n"
                client.send(data.encode("utf-8"))
    client.close()
