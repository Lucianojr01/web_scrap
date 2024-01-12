import requests
from bs4 import BeautifulSoup
import pandas as pd

url_base = 'https://lista.mercadolivre.com.br/'

#produto_nome = input('qual nome do produto ')
produto_nome = 'bicicleta'
response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produto = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})

contador = 0

for produto in produto:

    titulo = produto.find('h2', attrs={'class': "ui-search-item__title"}) 
    link = produto.find('a', attrs={'class': "ui-search-item__group__element ui-search-link__title-card ui-search-link"})
    preço = produto.findNext('span', attrs={'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})

    print('titulo do produto: ', titulo.text)
    print()
    print('link do produto: ', link['href'])
    print()
    print('preço do produto: ', preço.text) 

    contador += 1

    print('\n\n')

print(f'Número total de iterações: {contador}')
print()