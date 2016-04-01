Read this before running the server program.
There is a user-friendly configuration file(ws.conf) associated with this Simple http server program.
The user can change the values and files supported by the server by making corresponding changes in the configuration file.
The content in ws.conf is as follows:
#serviceport number
Listen 
8097
#document root
DocumentRoot [You can change the root directory here]
"C:/Users/sathvik reddy/Documents/dcomm/www"
#default web page
DirectoryIndex index.html index.htm index.ws 
#Content-Type which the server handles
.html text/html[You can change files handled by the server here]
.htm text/html
.txt text/plain
.png image/png
.gif image/gif
.jpg image/jpg
.css text/css
.js  text/javascript
.ico image/x-icon

This server sends the data following TCP protocol. So, it first makes a connection with the client and then sends the data.
Types of errors handled are : 
1. Error 400 Invalid method
2. Error 400 Invalid URI
3. Error 400 Invalid HTTP version
4. Error 404 Not found
5. Error 500 Internal Server error
The supported files by this server are :
.html 
.htm 
.txt 
.png 
.gif 
.jpg 
.css 
.js  
.ico 
