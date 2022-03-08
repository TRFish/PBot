# Основной модуль бота
import config
import time

def input_analyzer(command):
	#Вывод приветствия
	if command == 'start':
		start()
	#Вывод списка команд
	elif command == 'help':
		help()
	#Режим диалога
	elif command == 'dialog':
		dialog()
	#Новый функционал, а точнее почему он не выходит
	elif command == 'new':
		new()
	#Новости бота
	elif command == 'news':
		news()
	#Echo-mode
	elif command == 'echo':
		echo_mode()
	#Nothing
	else:
		nothing()

def start():
	print('Привет, меня зовут ' + config.Name + ', бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши /help')

def help():
	print('Список команд пока не доступен')

def dialog():
	print('Режим разговора. Тут ты можешь действительно поболтать о чем угодно. Чтобы выйти напиши /exit')
	usr_text = input()
	while usr_text != 'exit':
		#Достижение(Скам мамонта №1)
		if config.A_Mamont_V == 0:
			print('Хаха\nТы думал, я сюда ИИ запихал?')
			print('Вы получили достижение: Мамонт заскамлен')
			config.A_Mamont_V = 1
			print('АХАХАХАХАХА')
		usr_text = input('\nДля выхода напиши"exit"\n')

def new():
	print('░▄▄▄▄░')
	print('▀▀▄██►')
	print('▀▀███►')
	print('░▀███►░█►')
	print('▒▄████▀▀')
	print('')
	print('Я сделяль новые функции, а это динозавр их стащил. Честно.')
	time.sleep(4)
	print('')
	print('───▄▄▄')
	print('─▄▀░▄░▀▄')
	print('─█░█▄▀░█')
	print('─█░▀▄▄▀█▄█▄▀')
	print('▄▄█▄▄▄▄███▀')
	print('Но я уже делаю новые со скоростью угашенной улитки!')

def news():
	print('Новое в Боте:')
	print('- _|__|_ \|Ничего|/ _|__|_ (Всё что не относится к другим командам):\nПо заголовку вы могли понять, что я ничего не добавил, но _|__|_ \|Ничего|/ _|__|_ это новая команда, которая выводит _|__|_ \|НИЧЕГО|/ _|__|_ !\nИ самое важное в этой команде она в добавок ко всему ничего не делает!')
	print('- Команда нового функционала (/new)\nВыводит честные причины долгого выхода обговлений.')
	print('- Echo-mode (/echo)\nПросто выводит то, что ты пишешь\nОсторожно! Выйти от туда немного затруднительно.')

def nothing():
	print('_|__|_ \|НИЧЕГО|/ _|__|_')

def echo_mode():
	text = ''
	while text != 'Stop. Please, stop!':
		while text != 'Please!':
			while text != 'please':
				while text != 'stop':
					text = input('Введите любой текст(Чтобы выйти напишите stop):')
					print(text)
				text = input('Введите любой текст(А волшебное слово):')
				print(text)
			text = input('Введите любой текст(Не расслышал):')
			print(text)
		text = input('Введите любой текст(А теперь всё вместе):')
		print(text)
	print('Ну ладно, ладно. Не бугурти.')
