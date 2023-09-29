import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1:
        break

    try:
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read()
        print('Retrieved', len(data), 'characters')

        tree = ET.fromstring(data)
        counts = tree.findall('.//count')

        total_count = 0
        for count in counts:
            total_count += int(count.text)

        print('Count:', len(counts))
        print('Sum:', total_count)

    except Exception as e:
        print('Error:', e)
