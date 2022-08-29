from asyncio import ensure_future, gather, get_event_loop
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import lxml

"""
Para fins de visualização, as funções abaixo são importados pelo arquivo do Jupyter Notebook "Avaliação_Mod09.py"
Caso queira executá-la em IDE's, tirar o comentário da linha 55 "#loop.run_until_complete(future)"
"""

async def fetch(session, url):
    """
    A função abaixo recebe o response da função run e ao passar a variável pelo Beautiful Soup,
    imprime todos os títulos das páginas contidas na lsita de urls.
    """
    async with ClientSession() as session:
        async with session.get(url) as response:
           text = await response.read()
           soup = BeautifulSoup(text.decode('utf-8'),"lxml")
           titles = soup.title.text
           print(titles)
           



async def run():
    """
    A função abaixo passa a lsita de urls pelos parâmetros definidos na função 'fetch' e cria uma lista
    Essa lista de dados passará pela funcão 'fetch', que realizará o parsing e retornará o título das páginas
    """
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
    tasks  = []
    async with ClientSession() as session: 
        for url in urls:
            task = ensure_future(fetch(session,url))
        tasks.append(task)

    await gather(*tasks)
        


loop = get_event_loop()
future = ensure_future(run())
#loop.run_until_complete(future)
