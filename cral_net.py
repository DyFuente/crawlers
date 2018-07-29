import requests
from bs4 import BeautifulSoup
import json
import ast
import time
url = 'https://programacao.netcombo.com.br/gatekeeper/canal/select?q=id_cidade:1&callback=callbackChannels&json.wrf=callbackChannels&wt=json&rows=5000&start=0&sort=categoria%20asc,cn_canal%20asc&fq=nome:*&_=&callback=callbackChannels'

list_of_channels_check = ['Universal Channel', 'Fox','Warner','Sony','FX','AXN','TBS','Comedy Central','A&E','ID','Syfy','Lifetime','AMC','Fox Premium 1 HD','Fox Premium 2 HD']


def get_my_objs(url):

	data = requests.get(url).text
	data = data[17:-1]
	data_dict = ast.literal_eval(data)
	objs = data_dict['response']['docs']  	
	return objs

def get_my_objs_template(channel_id):
	url_template = f'https://programacao.netcombo.com.br/gatekeeper/exibicao/select?q=id_revel:1_{channel_id}+&callback=callbackShows&json.wrf=callbackShows&wt=json&rows=100000&sort=id_canal%20asc,dh_inicio%20asc&fl=dh_fim%20dh_inicio%20st_titulo%20titulo%20id_programa%20id_canal&fq=dh_inicio:%5B2018-07-29T00:00:00Z%20TO%202018-08-30T23:59:00Z%5D&callback=callbackShows'
	data = requests.get(url_template).text
	data = data[14:-1]
	data_dict = ast.literal_eval(data)
	objs = data_dict['response']['docs']  	
	return objs

list_of_channels = get_my_objs(url)

list_of_channel_details = []
for obj in list_of_channels:
	for check in list_of_channels_check:
		if(obj['nome'] == check):
			list_of_channel_details.append(get_my_objs_template(obj['id_canal']))


with open('net_channels_info.json', 'w') as f:  
    json.dump(list_of_channel_details, f)
