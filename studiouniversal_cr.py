
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException  
import time
import jsonpickle
import json

browser = webdriver.Chrome("C:/Users/renan/Tutorial/chromedriver.exe")

browser.maximize_window()
browser.execute_script("document.body.style.zoom='100'")


# use the page source on Beautiful just like if it was done through requests.


list_of_channels = ['Canal Brasil',
 'Megapix',
 'Cinemax',
 'Prime Box Brazil',
 'Studio Universal',
 'Paramount'
 ] 

url = 'http://studiouniversal.globo.com/programacao.html'

browser.get(url)

#Using Xpath because I can iterate through the items. 
class Text():

		def __init__(self, time, subtitulo, complemento):
			self.time = time
			self.subtitulo = subtitulo
			self.complemento = complemento

def getItem(item, div, _class):
	if(item.find(div,class_=_class) == None):
		return 'Found No Item'	
	else:
		return item.find(div,class_=_class).text.strip()
def getObjct():
	items = soup.find_all('div', class_='episodio')
	for i in items:	
		b = Text(getItem(i,'span', 'hora'),
				getItem(i,'h5', 'subtitulo'),
				getItem(i,'p', 'complemento')
		)
		my_objects.append(b)

my_objects = []

for i in range(7,21):
	number = i
	next_button_xpath = '//span[@class="seta proximo"]//span[@class="icone"]'
	if(number < 11):
		xpath = f'//*[@id="area-background"]/main/div/div[2]/div[1]/div/ul/div/div/div[{number}]'
		delay = 3
		try:
		    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, xpath)))
		    print("Page is ready!")
		except TimeoutException:
		    print("Loading took too much time!")
		myElem.click() 
		time.sleep(2)

		# get the page_source.
		html_source = browser.page_source
		soup = bs.BeautifulSoup(html_source, "lxml")
		
		#Getting information about the movie
		getObjct()

	else:
		next_button_xpath = '//span[@class="seta proximo"]'
		browser.find_element_by_xpath(next_button_xpath).click()
		_xpath= f"//div[@class='owl-wrapper']//div[{number}]"
		time.sleep(2)
		browser.find_element_by_xpath(_xpath).click()
		# use the page source on Beautiful just like if it was done through requests.
		time.sleep(2)
		html_source = browser.page_source
		soup = bs.BeautifulSoup(html_source, "lxml")
		
		#Getting information about the movie
		getObjct()
		
# close the browser
browser.quit()
for i in my_objects:
	print(i.time)
	print(i.subtitulo)
	print(i.complemento)
	print("-------------------------")

# get class titulo to get either a movie/cinemao @@ whatever da fuck that shit is.
# get class subtitulo to get the titulo
# get class complemento for resumo
# get class classificacao for age restriction
# get class ano for year of the movie
# get class pais to get the origin of the movie
