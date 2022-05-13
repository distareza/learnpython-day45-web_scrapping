"""
Web Scrapping using BeautifulSoup4 (bs4)
"""
import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://distareza.github.io/cv/")
response.raise_for_status()

contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
#print content html element: <title></title>
print(soup.title)
