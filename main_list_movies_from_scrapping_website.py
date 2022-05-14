"""
    Scrapping a list of best 100 movie from empireonline.com
    and save into file
"""
import requests
from bs4 import BeautifulSoup

#url = "https://www.empireonline.com/movies/features/best-movies-2/"
url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url)
response.raise_for_status()

web_content = BeautifulSoup(response.text, 'html.parser')

movies = [anchor.getText() for anchor in web_content.select(selector="h3.title")]
ascending_movie = movies[::-1]

with open("movies.txt", mode="w") as file:
    for movie in ascending_movie:
        file.write(f"{movie}\n")
