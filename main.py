import requests
import html5lib
from bs4 import BeautifulSoup

url = "https://github.com/parthasdey2304/"
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')
print(soup.prettify())
