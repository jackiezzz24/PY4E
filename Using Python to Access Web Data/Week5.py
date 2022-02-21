# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum0 = 0
while True:
    url = input('Enter location: ')
    if len(url) < 1: break
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx).read()
    print('Retrieved', len(uh), 'characters')
    tree = ET.fromstring(uh)
    data = tree.findall('comments/comment')

    for item in data:
        num = item.find('count').text
        sum0 = int(num)+sum0
    print('Counts:', len(data))
    print('Sum:' ,sum0)
