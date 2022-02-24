from backend import *

# Выбор языка
while True:
	lang = input('Выберите язык:\n 1 - ru_RU | Русский\n 2 - en_US\nChoose: ')
	if lang == '2':
		from lang.en_US import *
		break
	else:
		from lang.ru_RU import *
		break

# Еще один безполезный комент объясняющий смысл и так понятного куска кода
command = '/start'
while command != '/exit':
	#Вывод приветствия
	if command == '/start':
		start()
	#Вывод списка команд
	elif command == '/help':
		help()
	#Режим диалога
	elif command == '/dialog':
		dialog()
	#Новый функционал, а точнее почему он не выходит
	elif command == '/new':
		new()
	#Новости бота
	elif command == '/news':
		news()
	#Echo-mode
	elif command == '/echo':
		echo_mode()
	#Nothing
	else:
		nothing()
	command = '/' + input('Command: ')