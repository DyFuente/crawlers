from bs4 import BeautifulSoup
import requests
import datetime
from calendar import monthrange

d = datetime.date.today()
starting_day = d.day
month = d.month - 1
max_days = monthrange(2018,month - 1)[1]
nextMonth = month + 1

list_of_movies = []

class Movie():

	def __init__(self, time, img_src, title, sinopse, day):
		self.time = time
		self.img_src = img_src
		self.title = title
		self.sinopse = sinopse
		self.day = day

def gotoNextMonth(nextMonth):
	for y in range(1,32):
		url = f'http://primeboxbrazil.com.br/l1/schedules/{y}-{nextMonth}'
		data = requests.get(url).text
		soup = BeautifulSoup(data,'lxml')
		
		if(soup.find('section', class_="coming-up") == None):
			print("couldn't find anythig bro, fck off")
			break
		else:
			getContent(soup, y)
			print('I found something uhul ;)')

def getContent(soup,day):
	main = soup.find_all('tr')
	for i in main:
		sub_main = i.find_all('td')
		time = sub_main[0].find('span', class_='title').text.strip()
		title = sub_main[1].find('span', class_='title').text.strip()
		img_src = sub_main[1].find('img').get('src')
		sinopse = sub_main[1].find('span', class_='synopsis').text.strip()
		obj = Movie(time,img_src,title,sinopse,day)
		list_of_movies.append(obj)


for i in range(starting_day, max_days+1):
	url = f'http://primeboxbrazil.com.br/l1/schedules/{i}-{month}'
	data = requests.get(url).text
	soup = BeautifulSoup(data,'lxml')
	getContent(soup, i)
	print('all good champs')
	if(i == max_days):
		print('done for this month.. Going to the next month bro')
		break

gotoNextMonth(nextMonth)
print(list_of_movies[-1].time)
print(list_of_movies[-1].img_src)
print(list_of_movies[-1].title)
print(list_of_movies[-1].sinopse)
print(list_of_movies[-1].day)

