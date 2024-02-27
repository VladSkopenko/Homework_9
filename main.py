from requests import Session
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'
with Session() as s:
    response = s.get(url)

soup = BeautifulSoup(response.text, "lxml")
quote = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

def save():
    with open("qoutes.json", "w", encoding="utf-8") as file:
        quotes = []
        for quot, author, tags_element in zip(quote, authors, tags):
            data = {
                "tags": tags_element.text.split()[1:],
                "author": author.text,
                "quote": quot.text,
            }
            quotes.append(data)
        json.dump(quotes, file, indent=4)



