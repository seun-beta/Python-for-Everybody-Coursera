''' Make a socket program that counts the number of characters it has received and stops 
displaying any text after it has shown 3000 characters. The program should retrieve the entire 
document and count the total number of characters and display the count of the number of characters 
at the end of the document.
 '''
import socket 
import ssl
import time 
url = input('Input URL: ')
split_url = url.split('/')
host = split_url[2]
port = 80 

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host,port))
command  = "GET " + url + " HTTP/1.0\r\n\r\n"
cmd = command.encode()
mysock.send(cmd)

while True :
    data = mysock.recv(3000)
    time.sleep(0.1)
    if len(data) < 1 : 
        break
    #print ('================================',len(data),'================================')
    information = data.decode()
print (len(information))
print (information[:3000])
