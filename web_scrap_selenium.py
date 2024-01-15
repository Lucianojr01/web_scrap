from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
#from selenium.webdriver.edge.options import Options

#options = Options()

#options.add_argument('window-size=400,800')

navegador = webdriver.Edge()

navegador.get('https://www.catho.com.br/vagas/')
sleep(3)
vaga = navegador.find_element(By.ID,'keyword')

vaga.send_keys('cientista de dados')

estado = navegador.find_element(By.ID,'location')
sleep(2)


estado.send_keys('Rio de Janeiro')
sleep(2)
primeira_sugestao = estado.find_element(By.TAG_NAME, "Rio de Janeiro/RJ")



sleep(1000)