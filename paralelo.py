from re import L
from requests import get
import lxml
from bs4 import BeautifulSoup

"""
Para fins de visualização, a funcão é importada e executada no arquivo Avaliação_Mod09.ipynb
"""

def scraper(url):
    """ 
    Os títulos das doze páginas elencadas na lista 'urls' serão raspados e impressos no Jupyter Notebook
    Utilizar arquivo Avaliação_Mod09.ipynb
    """
    crawl = get(url).text
    tags = BeautifulSoup(crawl, "lxml")
    page_title = tags.title.text.replace("\n","")
    print(page_title)


urls = [ "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "https://books.toscrape.com/catalogue/category/books/classics_6/index.html",
    "https://books.toscrape.com/catalogue/category/books/philosophy_7/index.html",
    "https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
    "https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html",
    "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html",
    "https://books.toscrape.com/catalogue/category/books/childrens_11/index.html",
    "https://books.toscrape.com/catalogue/category/books/religion_12/index.html",
    "https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
    "https://books.toscrape.com/catalogue/category/books/music_14/index.html"]
