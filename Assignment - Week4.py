import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
counts = int(input('Enter count:'))
pos = int(input('Enter position:'))
n = 0
while n < counts:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    n = n+1
    tag = tags[pos-1]
    url = tag.get('href',None)
    print('Retriveing:', tag.get('href',None))
