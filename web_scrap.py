import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')


content = response.content

site = BeautifulSoup(content, 'html.parser')

'''noticia = site.findAll('div',attrs={'class': 'feed-post-body'})

for noticia in noticia:

    titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})

    print(titulo.text)

    sub_titulo = noticia.find('span', attrs={'class' : 'feed-post-metadata-section'})

    if (sub_titulo):

        print(sub_titulo.text)
    print()'''