import socket
import re
import os
import select
import sys

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
input = [s]
run =1
while run:
    inputready,outputready,exceptready = select.select(input,[],[])
    print(inputready,outputready,exceptready)
    for s1 in inputready: 

        if s1 == s: 
            # handle the server socket 
            client, address = s.accept() 
            input1.append(client) 
        else:
            client, address = s1.accept()
            recd = client.recv(size)
            print(recd)
            if recd :
                data = recd.decode("utf-8")
                httpreqst= data.split()[0]
                print(httpreqst)
                requestedfile= data.split()[1]
                print(requestedfile)
                httpversion= data.split()[2]
                print(httpversion)
                connectiontype= data.split()[6]
                if (httpreqst != 'GET'):
                    data= " Error400 : Invalid method"
                    print(data)
                    client.send(data.encode("utf-8"))
                elif checkinvalidurl(requestedfile) : #function not defined
                    data= "Error400 : Invalid URI"
                    print(data)
                    client.send(data.encode("utf-8"))
                elif httpversion != 'HTTP/1.1':
                    data= "Error400: Invalid HTTP-version"
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
                    print(fileextnsn)
                    if substringinstring(fileextnsn, configfile_string):
                        data= "Error 501: file not supported"
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
                            data= "Error 404: Not found"
                            client.send(data.encode("utf-8"))
                        s1.send(header.encode("utf-8"))
                        s1.send(data1)
            else:
                s1.close()
                input1.remove(s1)
        client.close()
