import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


# Function to retrieve the href values from anchor tags in a given URL
def get_links(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for tag in soup('a'):
        links.append(tag.get('href', None))
    return links


# Input the starting URL, count, and position
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))

# Repeat the process for the specified number of times
for _ in range(count):
    print(f"Retrieving: {url}")
    links = get_links(url)

    # Check if the desired position is within the range of available links
    if position <= len(links):
        url = links[position - 1]  # Adjust for zero-based index
    else:
        print("Position exceeds the number of links on the page.")
        break

# Extract the last name from the final URL
if url:
    parts = url.split('/')
    last_name = parts[-1].split('.')[0]
    print(f"Last name in sequence: {last_name}")
