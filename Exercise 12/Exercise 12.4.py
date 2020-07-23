'''  Write a program to  
 extract and count paragraph (p) tags from 
 the retrieved HTML document and display the count of the paragraphs as the output
  of your program. Do not display the paragraph text, only count them. Test your 
  program on several small web pages as well as some larger web pages.
 '''
import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context() 
ctx.check_hostname = False 
ctx.verify_mode = ssl.CERT_NONE

user_input = 'https://docs.python.org'
url = urllib.request.urlopen(user_input, context=ctx).read()
data = url
soup = BeautifulSoup(data, 'html.parser')

p_tags = soup('p')
count = 0
for p_tag in p_tags :
    count += 1
    print(p_tag.get('href',None))
print (count)
