import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []

response = requests.get('https://br.1xbet.com/betsonyour/line/football/287089-brazil-campeonato-carioca')


content = response.content

site = BeautifulSoup(content, 'html.parser')

odes = site.find('div' ,attrs={'class': 'grayBack'})

noticia = odes.findAll('span',attrs={'class': 'c-events__team'})

'''for odes in odes:

    titulo = odes.find('span', attrs={'class' : 'c-events-time__val'})

    #print(titulo.text)

    sub_titulo = odes.find('span', attrs={'title': True})

    if (sub_titulo):
        lista_noticias.append([titulo.text, sub_titulo.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text, '' ,titulo['href']])    
    

news = pd.DataFrame(lista_noticias,columns=['Titulo', 'Subtitulo', 'Link'])    
print(news)'''

a = []
b = []
# Loop for para percorrer a lista de números pelos índices
for indice, numero in enumerate(noticia):
    if indice % 2 == 0:
        # Índice par, adicionar à variável 'b'
        b.append(numero)
    else:
        # Índice ímpar, adicionar à variável 'a'
        a.append(numero)

# Exibir resultados
print("Variável 'a' (soma de números em índices ímpares):", a)
print("Variável 'b' (soma de números em índices pares):", b)



times = pd.DataFrame(a,b, columns=['times','tt'])
print(times)