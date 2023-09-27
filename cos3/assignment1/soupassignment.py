import urllib.request
import ssl
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Initialize a variable to store the sum of numbers
total_sum = 0

# Find all the <span> tags with class "comments"
tags = soup.find_all('span', class_='comments')

# Iterate through the found <span> tags and add their contents (numbers) to the total_sum
for tag in tags:
    try:
        # Convert the content of the <span> tag to an integer and add it to the total_sum
        total_sum += int(tag.text)
    except ValueError:
        # Handle the case where the content of the <span> tag is not a valid integer
        pass

# Print the total sum of numbers
print("Total Sum of Numbers:", total_sum)
