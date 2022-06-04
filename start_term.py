#!/bin/python

import config
import time
import random
from image import aprint as image # почему я только СЕЙЧАС узнал про AS. (так блет я ща мультиязычность прикручу)

class Bot():
	def __init__(self, botType='Terminal'):
		self.bot_type  = botType
	
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
	
	def dialog(self):
		print(text.dialog_welcome)
		self.text = input('>> ')
		while self.text != 'exit':
			#Достижение(Скам мамонта №1)
			if config.A_Mamont_V == 0:
				print(text.dialog_rep1)
				print(text.ach_received, text.ach_mamont)
				config.A_Mamont_V = 1
				print(text.dialog_rep2)
			self.text = input(f'\n{text.tip_exit}:\n')
	
	def new(self):
		image('dino')
		print(text.new_rep1)
		time.sleep(0.1)
		print(text.new_rep2)
		time.sleep(4)
		image('snail')
		print(text.new_rep3)
	
	def echo_mode(self):
		self.text = None
		while self.text != 'Stop. Please, stop!':
			while self.text != 'Please!':
				while self.text != 'please':
					while self.text != 'stop':
						self.text = input(f'{text.tip_text} {text.echomode_rep1}')
						print(self.text)
					self.text = input(f'{text.tip_text} {text.echomode_rep2}')
					print(self.text)
				self.text = input(f'{text.tip_text} {text.echomode_rep3}')
				print(self.text)
			self.text = input(f'{text.tip_text} {text.echomode_rep4}')
			print(self.text)
		print(text.echomode_exit)
	
	def rando(self):
		self.minimal = int(input(text.rando_rep1))
		self.maximal = int(input(text.rando_rep2))
		self.output  = random.randint(self.minimal, self.maximal)
		print(self.output)
	
	def news(self):
		print(text.news_main)
	
	def help(self):
		print(text.help)
	
	def start(self):
		print(text.start)


if __name__ != '__main__':
	print(f'Использование бота ({config.Name}) как модуль другого проекта не предусмотренно!(ну и для чего я эту защиту сделал...)')
	exit()

# Lang chooser
lng = input('Choose language:\n 1 - Russian\n 2 - English\n>> ')
if lng == '1' or lng == '':
	from lang import ru_RU as text
elif lng =='2':
	from lang import en_US as text
else:
	print('Error')
	exit()

# Main
bot = Bot()
command = 'start'
while command != 'exit':
	bot.input_analyzer(command)
	command = input('>> ')
print(text.exit)
