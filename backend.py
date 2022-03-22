# Основной модуль бота
import config
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

import random
def rando():
	minimal = int(input('Минимальное число:'))
	maximal = int(input('Максимальное число:'))
	ran = random.randint(minimal, maximal)
	print(ran)
