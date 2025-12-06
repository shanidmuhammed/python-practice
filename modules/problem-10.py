# Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The program should print only the IP address and nothing else.

from urllib.request import urlopen
import json

def myip(url):
    content = urlopen(url).read().decode('utf-8')
    json_data = json.loads(content)
    print(json_data['origin'])

url = "http://httpbin.org/get"
myip(url)