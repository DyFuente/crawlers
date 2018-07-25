
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
list_of_channels = ['Canal Brasil',
 'Megapix',
 'Cinemax',
 'Prime Box Brazil',
 'Studio Universal',
 'Paramount'
 ] 

list_of_links = [ 'http://canalbrasil.globo.com/programacao.html',
'http://megapix.globo.com/',
'https://br.cinemax.tv/schedule',
'http://www.boxbrazil.tv.br/prime-box-brazil-grade-de-programacao/',
'http://studiouniversal.globo.com/programacao.html',
'https://www.netcombo.com.br/tv-por-assinatura/programacao/canal/paramount-447'
]

# Code for Canal Brasil!

# Get the link Canal Brasil
url = (list_of_links[0])
#Open the url with Selenium, since the data that I need is being rendered through Javascript,
#I have to use Selenium. 
browser.get(url)
#number that will control the days in the page. starting with 7 because it's the first day 

#store all the objects created
main_objs = []

#Using Xpath because I can iterate through the items. 
class Text():

		def __init__(self, subtitulo, complemento, classificacao,year,origin_country):
			self.subtitulo = subtitulo
			self.complemento = complemento
			self.classificacao = classificacao
			self.year = year
			self.origin_country = origin_country

my_text = []
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
		# get the page_source.
		myElem.click() 

		time.sleep(2)
		html_source = browser.page_source
		# close the browser
		# use the page source on Beautiful just like if it was done through requests.
		soup = bs.BeautifulSoup(html_source, "lxml")
		#Getting information about the movie
		items = soup.find_all('div', class_='episodio')
		for i in items:
			b = Text(i.find('h5', class_='subtitulo').text.strip(), 
					i.find('p', class_='complemento').text.strip(),
					i.find('span', class_='classificacao').text.split(),
					i.find('span', class_='ano').text.split(),
					i.find('span', class_='pais').text.split()
								)
			my_text.append(b)
	else:
		next_button_xpath = '//span[@class="seta proximo"]'
		_xpath= f"//div[@class='owl-wrapper']//div[{number}]"
		browser.find_element_by_xpath(next_button_xpath).click()
		time.sleep(5)
		browser.find_element_by_xpath(_xpath).click()
		html_source = browser.page_source
		# close the browser
		# use the page source on Beautiful just like if it was done through requests.
		soup = bs.BeautifulSoup(html_source, "lxml")
		#Getting information about the movie
		items = soup.find_all('div', class_='episodio')
		for i in items:
			b = Text(i.find('h5', class_='subtitulo').text.strip(), 
					i.find('p', class_='complemento').text.strip(),
					i.find('span', class_='classificacao').text.split(),
					i.find('span', class_='ano').text.split(),
					i.find('span', class_='pais').text.split()
								)
			my_text.append(b)
browser.quit()
my_file = jsonpickle.encode(my_text)

for i in my_text:
	print(i.subtitulo)
	print(i.complemento)
	print(i.classificacao)
	print(i.year)
	print(i.origin_country)
	print("-------------------------")
with open('text.json', 'w') as f:
	json.dump(my_file, f, indent=2, ensure_ascii=False)


#for i, c in enumerate(my_text):
#	print(c[i].classificacao)
# get class titulo to get either a movie/cinemao @@ whatever da fuck that shit is.
# get class subtitulo to get the titulo
# get class complemento for resumo
# get class classificacao for age restriction
# get class ano for year of the movie
# get class pais to get the origin of the movie






