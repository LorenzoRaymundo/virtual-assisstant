import time
import datetime
import json
import requests
from decimal import Decimal
import requests
from bs4 import BeautifulSoup

def get_weather(search):
	try:
		info = f'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q={city}'
		r = requests.get(info).json()
		acutual_temperature = r['main']['temp']
		acutual_temperature = acutual_temperature - 273,15
		temperature = Decimal("%.2f" % acutual_temperature[0])
		temperature = float(temperature) - (acutual_temperature[1]/100)
		temperature = int(temperature)

		speak(f'A temperatura em: {search} é de {temperature} °C')

	except:
		print(f'Não foi possível encontrar a temperatura de: {search}')

"""
city = input("City: ")
google_search = f'https://www.google.com/search?q={city}'
results = requests.get(google_search)
print(results.links)
"""
search='temperatura sao leopoldo'
search = search.split(' ')

if 'em' in search:
	for word in search:
		if word == 'em':
			index_word = search.index(word)
			print(index_word)
			search = search[index_word+1:]
else:
	search = search[1:]

search = ' '.join(search)
print(search)

def google_search(search):
	
	url = f'https://www.google.com/search?q={search}'
	req = requests.get(url).text

	soup = BeautifulSoup(req, 'lxml')

	#try: # pick up the top div and get the info
	info = soup.find_all('div')
	print(info)

	for div in info:
		if div['class'] == 'kno-rdesc':
			info = div.text

	print(info)
	print('nothing')
		# info = soup.find('div', class_='UDZeY OTFaAf')
	#except: # goto the right side div
		#print('no')

google_search('abacaxi')