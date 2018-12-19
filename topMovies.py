""" Scrape IMBD website for most popular movies of a certain year and display
    the titles of the movies.
    IMBD website: https://www.imdb.com/search/title?release_date=2018
    Sources of help: https://medium.com/@nishantsahoo/which-movie-should-i-watch-5c83a3c0f5b1
"""

import requests
from bs4 import BeautifulSoup

year = input("Which year would you like to see? ")
page = requests.get("https://www.imdb.com/search/title?release_date=" + year)
soup = BeautifulSoup(page.content, 'html.parser')

movies = soup.findAll('div', attrs={'class':'lister-item mode-advanced'})

for div_item in movies:
    div = div_item.find('div', attrs={'class':'lister-item-content'})
    header = div.findChildren('h3', attrs={'class':'lister-item-header'})
    title_block = header[0].findChildren('a')
    title = title_block[0].get_text()
    print(title)
