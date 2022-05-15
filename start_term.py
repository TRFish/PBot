#!/bin/python

import config
import time
import random
import text_images

class Bot():
	def __init__(self, botType='Terminal'):
		self.bot_type  = botType
		self.t_nothing = '_|__|_ \|НИЧЕГО|/ _|__|_'
		self.t_start   = 'Привет, меня зовут ' + config.Name + ', бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши help'
		self.t_help    = 'Список команд пока не доступен'
		self.t_news    = 'Новое в Боте:\nНичего?'
	
	def input_analyzer(self, command):
		command = command.lower()
		
		# Вывод приветствия
		if command   == 'start':
			self.start()
		
		# Вывод списка команд
		elif command == 'help':
			self.help()
		
		# Режим диалога
		elif command == 'dialog':
			self.dialog()
		
		# Новый функционал, а точнее почему он не выходит
		elif command == 'new':
			self.new()
		
		# Новости бота
		elif command == 'news':
			self.news()
		
		# Echo-mode
		elif command == 'echo':
			self.echo_mode()
		
		# Random
		elif command == 'rand' or command == 'random':
			self.rando()
		
		# Nothing
		elif command == 'nothing':
			self.nothing()
	
	def dialog(self):
		print('Режим разговора. Тут ты можешь действительно поболтать о чем угодно. Чтобы выйти напиши "exit"')
		self.text = input()
		while self.text != 'exit':
			#Достижение(Скам мамонта №1)
			if config.A_Mamont_V == 0:
				print('Хаха\nТы думал, я сюда ИИ запихал?')
				print('Вы получили достижение: Мамонт заскамлен')
				config.A_Mamont_V = 1
				print('АХАХАХАХАХА')
			self.text = input('\nДля выхода напиши "exit":\n')
	
	def new(self):
		print(text_images.dino, '\nЯ сделяль новые функции, а это динозавр их сломал')
		time.sleep(0.1)
		print('Честно\n')
		time.sleep(4)
		print(text_images.snail, 'Но я уже делаю новые со скоростью угашенной улитки!')
	
	def echo_mode(self):
		self.text = None
		while self.text != 'Stop. Please, stop!':
			while self.text != 'Please!':
				while self.text != 'please':
					while self.text != 'stop':
						self.text = input('Введите любой текст(Чтобы выйти напишите stop):')
						print(self.text)
					self.text = input('Введите любой текст(А волшебное слово):')
					print(self.text)
				self.text = input('Введите любой текст(Не расслышал):')
				print(self.text)
			self.text = input('Введите любой текст(А теперь всё вместе):')
			print(self.text)
		print('Ну ладно, ладно. Не бугурти.')
	
	def rando(self):
		self.minimal = int(input('Минимальное число:'))
		self.maximal = int(input('Максимальное число:'))
		self.output  = random.randint(self.minimal, self.maximal)
		print(self.output)
	
	def news(self):
		print(self.t_news)
	
	def help(self):
		print(self.t_help)
	
	def start(self):
		print(self.t_start)
	
	def nothing(self):
		print(self.t_nothing)


bot = Bot()
command = 'start'
while command != 'exit':
	bot.input_analyzer(command)
	command = input('>> ')
print('Bye!')
