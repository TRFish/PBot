#!/bin/python

import config
import time
import random

class Bot():
	def __init__(self, botType=None):
		self.bot_type = botType
		self.nothing = '_|__|_ \|НИЧЕГО|/ _|__|_'
		self.start_text = 'Привет, меня зовут ' + config.Name + ', бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши /help'
		self.help_text = 'Список команд пока не доступен'
		self.news_text = 'Новое в Боте:\n- _|__|_ \|Ничего|/ _|__|_ (Всё что не относится к другим командам):\nПо заголовку вы могли понять, что я ничего не добавил, но _|__|_ \|Ничего|/ _|__|_ это новая команда, которая выводит _|__|_ \|НИЧЕГО|/ _|__|_ !\nИ самое важное в этой команде она в добавок ко всему ничего не делает!\n- Команда нового функционала (/new)\nВыводит честные причины долгого выхода обговлений.\n- Echo-mode (/echo)\nПросто выводит то, что ты пишешь\nОсторожно! Выйти от туда немного затруднительно.'

	def input_analyzer(self, command):
		command = command.lower()
		#Вывод приветствия
		if command == 'start':
			print(self.start_text)
		#Вывод списка команд
		elif command == 'help':
			print(self.help_text)
		#Режим диалога
		elif command == 'dialog':
			self.dialog()
		#Новый функционал, а точнее почему он не выходит
		elif command == 'new':
			self.new()
		#Новости бота
		elif command == 'news':
			print(self.news_text)
		#Echo-mode
		elif command == 'echo':
			self.echo_mode()
		#random
		elif command == 'rand' or command == 'random':
			self.rando()
		#Nothing
		elif command == 'ничего':
			print(self.nothing)

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
		output = random.randint(minimal, maximal)
		print(output)

bot = Bot()
command = 'start'
while command != 'exit':
	bot.input_analyzer(command)
	command = input('>> ')