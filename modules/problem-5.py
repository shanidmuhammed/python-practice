# Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

from urllib.request import urlopen
import sys

def wget_url(url):
    response = urlopen(url)
    if url.endswith('/'):
        filename = 'index.html'
    else:
        filename = url.split('/')[-1]

    with open(filename, 'wb') as f:
        f.write(response.read())

url = sys.argv[1]
wget_url(url)