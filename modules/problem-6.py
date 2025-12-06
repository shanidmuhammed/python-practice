from urllib.request import urlopen
import sys

def antihtml(url):
    response = urlopen(url).read().decode('utf-8')
    response = response.replace('<', "").replace('>', "")
    print(response)

antihtml(sys.argv[1])
