#!/bin/python

import config
import time
import random

class Bot():
	def __init__(self, botType):
		self.bot_type = botType

	def input_analyzer(self, command):
		#Вывод приветствия
		if command == 'start':
			self.start()
		#Вывод списка команд
		elif command == 'help':
			self.help()
		#Режим диалога
		elif command == 'dialog':
			self.dialog()
		#Новый функционал, а точнее почему он не выходит
		elif command == 'new':
			self.new()
		#Новости бота
		elif command == 'news':
			self.news()
		#Echo-mode
		elif command == 'echo':
			self.echo_mode()
		#random
		elif command == 'rand' or command == 'random':
			self.rando()
		#Nothing
		else:
			self.nothing()

	def start(self):
		print('Привет, меня зовут ' + config.Name + ', бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши /help')

	def help(self):
		print('Список команд пока не доступен')

	def dialog(self):
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

	def new(self):
		print('░▄▄▄▄░')
		print('▀▀▄██►')
		print('▀▀███►')
		print('░▀███►░█►')
		print('▒▄████▀▀')
		print('')
		print('Я сделяль новые функции, а это динозавр их сломал')
		time.sleep(0.1)
		print('Честно')
		time.sleep(4)
		print('')
		print('───▄▄▄')
		print('─▄▀░▄░▀▄')
		print('─█░█▄▀░█')
		print('─█░▀▄▄▀█▄█▄▀')
		print('▄▄█▄▄▄▄███▀')
		print('Но я уже делаю новые со скоростью угашенной улитки!')

	def news(self):
		print('Новое в Боте:')
		print('- _|__|_ \|Ничего|/ _|__|_ (Всё что не относится к другим командам):\nПо заголовку вы могли понять, что я ничего не добавил, но _|__|_ \|Ничего|/ _|__|_ это новая команда, которая выводит _|__|_ \|НИЧЕГО|/ _|__|_ !\nИ самое важное в этой команде она в добавок ко всему ничего не делает!')
		print('- Команда нового функционала (/new)\nВыводит честные причины долгого выхода обговлений.')
		print('- Echo-mode (/echo)\nПросто выводит то, что ты пишешь\nОсторожно! Выйти от туда немного затруднительно.')

	def nothing(self):
		print('_|__|_ \|НИЧЕГО|/ _|__|_')

	def echo_mode(self):
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

	def rando(self):
		minimal = int(input('Минимальное число:'))
		maximal = int(input('Максимальное число:'))
		ran = random.randint(minimal, maximal)
		print(ran)

bot = Bot()
command = 'start'
while command != 'exit':
	bot.input_analyzer(command)
	command = input('>> ')