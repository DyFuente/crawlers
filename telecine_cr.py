import bs4 as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  
import time
import jsonpickle
import json


#browser configuration first.  zoom at 100 because the chromedriver has a problem and stets the zoom to 90 fro some reason.
#Need to especify your own location for the WebDriverWait
browser = webdriver.Chrome("C:/Users/renan/Tutorial/chromedriver.exe")
#browser.maximize_window()
browser.execute_script("document.body.style.zoom='100'")

url = 'http://telecine.globo.com/programacao/'

browser.get(url)


def getContent():
	soup = get_source()
	grade_horas = soup.find_all('section', class_='grade-hora')
	for i in grade_horas:
		horario_grade =	i.find('span',class_='horario-grade').text.strip()
		titulo = i.find('strong', class_="titulofilme").text.strip()
		sinopse = i.find('p', class_="sinopse").text.strip()
		channel = i.find('img').get('title').strip()
		obj = {}
		obj['channel'] = channel
		obj['horario-grade'] = horario_grade
		obj['titulo'] = titulo
		obj['sinopse'] = sinopse
		list_of_movies.append(obj)

def get_len_menu():
	soup = get_source()
	len_menu_itens = len(soup.find_all('li', class_='jcarousel-item-horizontal'))
	return len_menu_itens

def get_source():
	html_source = browser.page_source
	soup = bs.BeautifulSoup(html_source,'lxml')
	return soup

def click_next():
	menu = browser.find_element_by_class_name(f'jcarousel-item-{i}-horizontal')
	menu.click()

list_of_movies = []

for i in range(31,get_len_menu()+1):
	click_next()	
	time.sleep(2)
	getContent()

with open('telecine_info.json', 'w') as f:  
    json.dump(list_of_movies, f)
