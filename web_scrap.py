import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')
response2 = requests.get('https://www.walissonsilva.com./')

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticia = site.find('div',attrs={'class': 'feed-post-body'})

titulo = noticia.find('a', attrs={'class' : 'feed-post-link'})
sub_titulo = noticia.find('span', attrs={'class' : 'feed-post-metadata-section'})

print(titulo.text)
print(sub_titulo.text)