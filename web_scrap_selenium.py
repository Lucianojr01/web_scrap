from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.edge.options import Options

#options = Options()

#options.add_argument('window-size=400,800')

navegador = webdriver.Edge()

navegador.get('https://www.catho.com.br/vagas/')
sleep(3)
vaga = navegador.find_element(By.ID,'keyword')

vaga.send_keys('analista')
vaga.send_keys(Keys.RETURN)

estado = navegador.find_element(By.ID,'location')

estado.clear()
estado.send_keys("rio de janeiro")
sleep(2)

estado.send_keys(Keys.RETURN)

sleep(2)
sleep(1000)