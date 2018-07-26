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
#Need to especify your own location for the webdriver
browser = webdriver.Chrome("C:/Users/renan/Tutorial/chromedriver.exe")
#browser.maximize_window()
browser.execute_script("document.body.style.zoom='100'")

url = 'http://megapix.globo.com/programacao/'

browser.get(url)


def getContent():
	soup = get_source()
	grade_horas = soup.find_all('li', class_='grade-hora')
	for i in grade_horas:
		horario_grade =	i.find('span',class_='horario-grade').text.strip()
		img_src = i.find('img').get('src')
		titulo = i.find('h3', class_="titulo cl").text.strip()
		sinopse = i.find('p', class_="sinopse").text.strip()
		obj = Movie(horario_grade,img_src,titulo,sinopse)
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
	#soup = get_source()		
	menu = browser.find_element_by_class_name(f'jcarousel-item-{i}-horizontal')
	menu.click()
#00048381112

list_of_movies = []

class Movie():

		def __init__(self, time, img_src, titulo_cl, sinopse):
			self.time = time
			self.img_src = img_src
			self.titulo_cl = titulo_cl
			self.sinopse = sinopse

for i in range(31,get_len_menu()+1):
	click_next()	
	time.sleep(2)
	getContent()

print(list_of_movies[-1].time)
print(list_of_movies[-1].img_src)
print(list_of_movies[-1].titulo_cl)
print(list_of_movies[-1].sinopse)
print("-------------------")
