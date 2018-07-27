import bs4 as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  
import time
import jsonpickle

browser = webdriver.Chrome("C:/Users/renan/Tutorial/chromedriver.exe")
browser.maximize_window()
browser.execute_script("document.body.style.zoom='100'")

url = 'https://br.cinemax.tv/schedule'

browser.get(url)

list_of_movies = []

class Movie():

	def __init__(self, time, img_src, titulo, sinopse, date):
		self.time = time
		self.img_src = img_src
		self.titulo = titulo
		self.sinopse = sinopse
		self.date = date

def get_source():
	html_source = browser.page_source
	soup = bs.BeautifulSoup(html_source,'lxml')
	return soup

def btnOpenAll():
	browser.find_element_by_id('gridOpenAll').click()

def getContent():
	soup = get_source()
	gridRow = soup.find_all('tr', class_='gridRow')
	GridSinopsisContainer = soup.find_all('div', { 'id': 'GridSinopsisContainer'})
	temp_list_gridRow = []
	temp_list_GridSinopsisContainer = []
	date = soup.find('spam', class_='gridMes left').text.strip()
	for i in gridRow:
		time =	i.find('th',class_='gridHora').text.strip()
		titulo = i.find('div', {'id':'xxxtitulo'}).text.strip()
		temp_list_gridRow.append(time)
		temp_list_gridRow.append(titulo)
	for y in GridSinopsisContainer:
		img_src = y.find('img').get('src')
		sinopse = y.find('p', class_="gridSinopsisTxt").text.strip()
		temp_list_GridSinopsisContainer.append(sinopse)
		temp_list_GridSinopsisContainer.append(img_src)
	createObjects(temp_list_gridRow,temp_list_GridSinopsisContainer, date)
	

def createObjects(_array1, _array2, date):
	for i in range(0,len(_array1),2):
		if(i == len(_array1)-1):
			break
		else:
			time = _array1[i]
			sinopse = _array2[i+1]
			img_src = _array2[i]
			titulo = _array1[i+1]
			obj = Movie(time,img_src,titulo,sinopse,date)
			list_of_movies.append(obj)


def btnOpenDay(number):
	number
	browser.find_element_by_id(f'{number}').click()

for i in range(27,32):
	btnOpenDay(i)
	time.sleep(3)
	btnOpenAll()
	time.sleep(3)
	getContent()

print(len(list_of_movies))
print(list_of_movies[-1].time)
print(list_of_movies[-1].img_src)
print(list_of_movies[-1].titulo)
print(list_of_movies[-1].sinopse)
print(list_of_movies[-1].date)
print('----------------------')
