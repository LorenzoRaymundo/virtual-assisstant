# MY VIRTUAL ASSISTANT v.1
# made by Lo, 2021
import time
import datetime
from user_commands import *


def assistant_exists():
	name = getAssis_name()
	if name == "":
		return False
	else:
		return True


def create_assistant():
	speak("Olá! Prazer em te conhecer!")
	speak("Parece que é a primeira vez que nos vemos")

	speak("Qual será meu nome?")
	assistant_name = listen(ignore=False)

	speak(f"OK! {assistant_name} parece interessante!")
	speak(f"Para me chamar, fale: {assistant_name}")

	with open('assistant.json', 'r') as f:
		data = json.load(f)
	
	data['assistantName'] = assistant_name

	with open('assistant.json', 'w') as json_file:
		json.dump(data, json_file)


def getAssis_name():
	with open('assistant.json', 'r') as f:
		data = json.load(f)
		name = data['assistantName']
		name = str(name)
		return name

# main function
def main():
	name = getAssis_name()
	called = 0
	WAKE = f"{name}"
	QUIT = f"até logo {name}"

	WHEATER_OPT = ['clima', 'temperatura', 'graus']
	HELP_OPT = ['quais comandos', 'lista de comandos', 'comandos', 'ajuda']
	ASSISSPEAK_OPT = ['Fale', 'diga', 'repita', 'repete']
	CHANGEASSISNAME_OPT = ['trocar', 'mudar nome', 'mudar o nome']
	CLEAN_OPT = ['pano', 'passar', 'casa', 'limpar']

	while True:
		print("listening...")
		queue = listen()
		if queue.count(WAKE) > 0:
			called += 1

			if called == 1:
				# get the actual time according to the operacional sistem time
				now = int(datetime.datetime.now().hour)

				if now >= 7 and now <= 12:
					speak("Bom dia!")

				elif now >= 12 and now < 18:
					speak("Boa tarde!")

				elif now >= 18:
					speak("Boa noite!")

			# main commands -->
			speak("sim, o que deseja?")
			waiting = listen(ignore=False)

			command(CHANGEASSISNAME_OPT, changeAssisName, waiting)
			command(ASSISSPEAK_OPT, assistant_speak, waiting)
			command(HELP_OPT, say_avaliable_commands, waiting)
			
			for option in WHEATER_OPT:
				if waiting.count(option) > 0:
					get_weather(waiting)

		elif QUIT in queue:
			speak("adeus!")
			break

# runs the program
if __name__ == '__main__':
	time.sleep(0.2)
	print('='*35)
	time.sleep(0.3)
	print('Assistente Virtual feito por Lo')
	time.sleep(0.3)
	print('='*35)
	time.sleep(0.5)

	assistant_exists = assistant_exists()
	if assistant_exists == False or None:
		create_assistant()

	main()