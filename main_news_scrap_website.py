import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

yc_content = response.text
soup = BeautifulSoup(yc_content, "html.parser")

print( soup.title )

#list all news title inside anchor element that having class "titlelink"
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
article_upvotes = []
for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)

article_upvotes = [ int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_texts)
# print(article_links)
# print(article_upvotes)

#Get the highest score of the article
highest_score = max(article_upvotes)
article_index = article_upvotes.index(highest_score)
popular_article = article_texts[article_index]
popular_link = article_links[article_index]
print(popular_article)
print(popular_link)