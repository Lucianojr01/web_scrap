import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []

response = requests.get('https://g1.globo.com/')


content = response.content

site = BeautifulSoup(content, 'html.parser')

noticia = site.findAll('div',attrs={'class': 'feed-post-body'})

for noticia in noticia:

    titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})

    #print(titulo.text)

    sub_titulo = noticia.find('span', attrs={'class' : 'feed-post-metadata-section'})

    if (sub_titulo):
        lista_noticias.append([titulo.text, sub_titulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '' ,titulo['href']])    
    

news = pd.DataFrame(lista_noticias,columns=['Titulo', 'Subtitulo', 'Link'])    
print(news)
print()