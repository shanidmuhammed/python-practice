# Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.

import sys
from urllib.request import urlopen
import re

def links(url):
    response = urlopen(url).read().decode('utf-8').split()
    for res in response:
        if res.startswith("href"):
            print(res)

links(sys.argv[1])
