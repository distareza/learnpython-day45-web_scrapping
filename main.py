"""
Web Scrapping using BeautifulSoup4 (bs4)
"""
import requests
from bs4 import BeautifulSoup
import lxml

response = requests.get("https://distareza.github.io/cv/about-me.html")
response.raise_for_status()

contents = response.text

soup = BeautifulSoup(contents, 'html.parser')

#print html element: <title></title>
print(soup.title)

#print content element: <title></title>
print(soup.title.string)

#print 1st element of html element <p>
print(soup.p)

#print all element of html element <p>
print(soup.find_all(name="p"))

#print attribute value of 1st anchor element
print(soup.find_all("a")[0].get("href"))

#print value attribute href from first <link> element
print(soup.find(name="link").get("href"))

#print all <h1> element that having id="name"
print(soup.find_all(name="h1", id="name"))

#print all <p> element that having class "footer-link"
print(soup.find_all(name="a", class_="footer-link"))

#print first element that match or having <span> inside <h2>
print(soup.select_one(selector="h2 span"))

#print all element that having attribute class "skill-image"
print(soup.select(selector=".skill-image"))

#print all element that having attribute id "name"
print(soup.select(selector="#name"))

