import speech_recognition as sr
import pyttsx3 as ptts
import time
import os
import json
import requests
from gtts import gTTS
from playsound import playsound
from decimal import Decimal
from bs4 import BeautifulSoup

def speak(text):
	engine = ptts.init('sapi5')
	engine.say(text)
	engine.runAndWait()

def listen(ignore=True):
	# defines what will recognize the voice
	r = sr.Recognizer()
	done = False

	while not done:
		# defines microfone
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=1) # adjust to the ambient noise
			audio = r.listen(source) # define to start listening
			output = ''

		# tries to recognize the voice
		try:
			output = r.recognize_google(audio, language="pt-BR")
			output = output.lower()
			print(output)
			done = True
		except sr.UnknownValueError:
			if ignore:
				pass
			else:
				speak("Não entendi.")

	return output


def command(opt_list, func, listening, show=False):
	for opt in opt_list:
		if listening.count(opt) > 0:
			func()
	if show == True:
		print(f'Debug: function {func} realized')

# USER OPTIONS
def assistant_speak(text=True):
	if text == True:
		while True:
			try:
				listening = str(input("Digite o texto para falar: "))
				speak(listening)
				break
			except ValueError or TypeError:
				print("Não entendi")
				time.sleep(.5)
	else:
		listening = listen(ignore=False)
		time.sleep(.7)
		speak(listening)


def changeAssisName():
	speak("Vamos trocar meu nome!")
	speak("E qual será meu novo nome?")

	assistant_name = listen(ignore=False)
	print(assistant_name)

	speak(f"OK! {assistant_name} parece interessante!")
	speak(f"Para me chamar, fale: {assistant_name}")
	speak(f"Observação: eu só irei atender por {assistant_name} caso o usuário reinicie o programa.")

	with open('assistant.json', 'r') as f:
			data = json.load(f)
		
	data['assistantName'] = assistant_name

	with open('assistant.json', 'w') as json_file:
		json.dump(data, json_file)


def say_avaliable_commands():
	valid_commands = ('Trocar nome', 'dizer algo, como um texto digitado ou repetir o que o usuario disse')
	penultimate_opt = len(valid_commands)-2

	speak("Os comandos dispoíveis são:")
	for i, command in enumerate(valid_commands):
		speak(command)
		if i == penultimate_opt:
			speak("e")


def get_weather(search):
	# gets the shitty info
	city = search
	url = f'https://www.google.com/search?q={city}'

	r = requests.get(url)

	soup = BeautifulSoup(r.text, 'html.parser')
	temperature = soup.find('div', class_='BNeawe').text

	# filters only the city
	search = search.split(' ')
	if 'em' in search:
		for word in search:
			if word == 'em':
				index_word = search.index(word)
				search = search[index_word+1:]
	else:
		search = search[1:]
	search = ' '.join(search)

	speak(f'A temperatura em: {search} é de {temperature} .')


def clean_house():
	speak('Vou passar pano é no teu rabo')