
import bs4 as bs
from selenium import webdriver  
browser = webdriver.Chrome("C:/Users/renan/Tutorial/chromedriver.exe")

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
# get the page_source. 
html_source = browser.page_source
# close the browser
browser.quit()
# use the page source on Beautiful just like if it was done through requests.
soup = bs.BeautifulSoup(html_source, "lxml")

#Getting information about the movie
main_div = soup.find('div', class_='horas')
items = main_div.find_all('div', class_='texto')

my_text = []
class Text():

	def __init__(self, subtitulo, complemento):
		self.subtitulo = subtitulo
		self.complemento = complemento

for i in items:
	my_text.append(Text(i.h5.text.strip(), i.p.text.strip()))

print(my_text[0].subtitulo)
# get class titulo to get either a movie/cinemao @@ whatever da fuck that shit is.
# get class subtitulo to get the titulo
# get class complemento for resumo
# get class classificacao for age restriction
# get class ano for year of the movie
# get class pais to get the origin of the movie







