# Create a new virtualenv and install BeautifulSoup. BeautifulSoup is very good library for parsing HTML. Try using it to extract all HTML links from a webpage.

from bs4 import BeautifulSoup
from urllib.request import urlopen

def extract_link(url):
    content = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

url = "https://www.w3schools.com/html/html_links.asp"
extract_link(url)