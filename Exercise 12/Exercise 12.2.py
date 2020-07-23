import urllib.request 
import time 
import ssl 
user_input = input('Input URL: ')
url = urllib.request.urlopen(user_input).read()
data = url.decode()

print (data[:3000])
print (len(data[:3000]))
print ('========', len(data), '========')






