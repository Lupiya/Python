import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.verify_mode =ssl.CERT_NONE

url = input('Enter -')
html = urllib.request.urlopen(url, context= ctx).read()
soup = BeautifulSoup(html, 'html.parser')  # Cleans up all the internal nasty bits that come with html

# Retrieve all of the anchor tags.
# The <a> tag (anchor tag) in HTML is used to create a hyperlink on the webpage
# This hyperlink is used to link the webpage to other web pages or some section of the same web page.
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
