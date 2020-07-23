import socket 

url = input('Input the url: ')
port = int(input ('Input port: '))

split_url = url.split('/')
try:
    host = split_url[2]
except:
    print ('The url is not correct')
    quit()


mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    mysock.connect((host,port))
except:
    print ('Cannot use host')
cmd = 'GET ' + url + ' HTTP/1.0 \r\n\r\n'
command = cmd.encode()
print (command)
try:
    mysock.send(command)
except:
    print ('The url is faulty')

