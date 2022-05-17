"""
    Web Scrapping using BeautifulSoup4 (bs4)
    Extract Upcomming Events in https://www.python.org into dictionary
"""
import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.python.org/")
response.raise_for_status()

contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
upcoming_event_element = soup.select_one("div.event-widget")

events = [{'time': el.select_one("time").get("datetime"), 'name': el.select_one("a").text} for el in upcoming_event_element.select("li")]
#events = [ { idx: {'time': el.select_one("time").text, 'name': el.select_one("a").text}  } for idx, el in enumerate( upcoming_event_element.select("li") ) ]

#print(events)
eventList = {}
for n in range(len(events)):
    eventList[n] = events[n]
print(eventList)
