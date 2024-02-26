import requests
from bs4 import BeautifulSoup
import pandas as pd 

lista_noticias = []

response = requests.get('https://br.1xbet.com/betsonyour/line/football/287089-brazil-campeonato-carioca')


content = response.content

site = BeautifulSoup(content, 'html.parser')

odes = site.find('div' ,attrs={'class': 'grayBack'})

noticia = odes.findAll('span',attrs={'class': 'c-events__team'})


times_da_casa = []
times_visitante = []
# Loop for para percorrer a lista de números pelos índices
for indice, numero in enumerate(noticia):
    if indice % 2 == 0:
        # Índice par, adicionar à variável 'b'
        times_da_casa.append(numero)
    else:
        # Índice ímpar, adicionar à variável 'a'
        times_visitante.append(numero)

df1 = pd.DataFrame(times_da_casa, columns=['Time da Casa'])
df2 = pd.DataFrame(times_visitante, columns=['Time Visitante'])
times = pd.concat([df1,df2], axis=1,)

noticia2 = odes.findAll('a',attrs={'class': 'c-bets__bet c-bets__bet_coef c-bets__bet_sm'})
noticia22 = odes.findAll('span',attrs={'class': 'c-bets__inner'})
vitoria_casa = [0, 18, 36, 54, 72, 90, 108, 126, 144, 162]

empate = [1, 19, 37, 55, 73, 91, 109, 127, 145,163]

vitoria_visi =[2, 20, 38, 56, 74, 92, 110, 128 ,146, 164]

win_casa =[]
drown = []
win_visi = []
# Iterar sobre os índices
for index,valor in enumerate(noticia22):
    if index in vitoria_casa:
        win_casa.append(valor)
    if index in empate:
        drown.append(valor)
    if index in vitoria_visi:
        win_visi.append(valor)


df3 = pd.DataFrame(win_casa, columns=['Time da Casa Vencendo'])
df4 = pd.DataFrame(drown, columns=['Empate'])
df5 = pd.DataFrame(win_visi, columns=['Time visitante Vencendo'])
odes_site = pd.concat([times,df3,df4,df5], axis=1,)

print(odes_site)
print(df2)
nome = 'luciano'
sobrenome = 'junior'