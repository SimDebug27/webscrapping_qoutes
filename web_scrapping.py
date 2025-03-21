from bs4 import BeautifulSoup
import requests
import pandas as pd

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

dataQuotes = []

#For loop for qoutes
for quote, author, tag in zip(quotes, authors, tags):
    dataQuotes.append([quote.text, author.text])

df = pd.DataFrame(dataQuotes, columns=['Quotes', 'Authors'])

df.to_csv('qoutes.csv', index=False, sep="\t", encoding='utf-8')