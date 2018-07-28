import requests 
import json
from bs4 import BeautifulSoup

month = 7
day = 28
url = f'https://programacao.netcombo.com.br/gatekeeper/exibicao/select?q=id_cidade:1&callback=callbackExhibitions&json.wrf=callbackExhibitions&wt=json&rows=10000&sort=dh_inicio+asc&fl=dh_inicio+st_titulo+titulo+id_programa+id_canal+fl_ppv+id_exibicao&fq=dh_inicio%3A%5B2018-{month}-{day}T16%3A32%3A26Z+TO+2018-08-28T16%3A32%3A26Z%5D&fq=id_canal%3A447&_=1532788303739'
resp = requests.get(url).text
dataform = resp.strip("callbackNextExhibitions(")
dataform = dataform.strip(")")
jsonData = json.loads(dataform)
full_data = jsonData['response']['docs']

def getSinopse(title, id_movie):
	sinopse = f'{title}-{id_movie}'
	return scrap_that(sinopse)

def scrap_that(sinopse):
	url_template_sinopse = f'https://www.netcombo.com.br/tv-por-assinatura/programacao/programa/{sinopse}'
	resp_sinopse = requests.get(url_template_sinopse).text
	soup = BeautifulSoup(resp_sinopse, 'lxml')
	try:
		item = soup.find('div', class_='description').p.text
		return item
	except AttributeError:
		return 'No sinopse found'
all_the_movies = []

for i in range(len(full_data)):
	obj = {}

	id_programa = full_data[i]['id_programa']
	titulo = full_data[i]['titulo']
	hour = full_data[i]['dh_inicio'][11:16]
	full_date = full_data[i]['dh_inicio'][:10]
	st_titulo = full_data[i]['st_titulo']
	sinopse = getSinopse(st_titulo, id_programa)

	obj['id_programa'] = id_programa
	obj['titulo'] = titulo
	obj['hour'] = hour
	obj['full_date'] = full_date
	obj['st_titulo'] = st_titulo
	obj['sinopse'] = sinopse
	all_the_movies.append(obj)

with open('paramount_info.json', 'w') as f:  
    json.dump(all_the_movies, f)