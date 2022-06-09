#!/bin/python

import time
import random
import sys
import config
from image import aprint as image

class Bot():
	def input_analyzer(self, command):
		command = command.lower()

		# Welcome_text
		if command   == 'start':
			self.start()

		# Output a list of commands
		elif command == 'help':
			self.help()

		# Dialog-mode
		elif command == 'dialog':
			self.dialog()

		# New functionality, or rather why it does not come out
		elif command == 'new':
			self.new()

		# Bot news
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
		del self.text

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
		del self.text
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


# Protection against using code as a module
if __name__ == '__main__':
	# Lang chooser
	try:
		arguments = sys.argv
		lng = arguments[1].lower()
		if lng == 'ru':
			import lang.ru_RU as text
		elif lng == 'en':
			import lang.en_US as text
		else:
			raise Exception('LanguageModulesAreNotConnected')
	except (TypeError, Exception):
		lng = input('Choose language (Выберите язык):\n 1 - Russian (Русский)\n 2 - English (Английский)\n(1) >> ')
		if lng == '1' or lng == '':
			import lang.ru_RU as text
		elif lng =='2':
			import lang.en_US as text
		else:
			raise Exception('LanguageModulesAreNotConnected')
	del arguments, lng

	# Main
	bot = Bot()
	command = 'start'
	while command != 'exit':
		bot.input_analyzer(command)
		command = input('>> ')
	print(text.exit)

else:
	print(f'Использование бота ({config.Name}) как модуль другого проекта не предусмотренно!(ну и для чего я эту защиту сделал...)')
	print(f'Using the bot ({config.Name}) as a module of another project is not provided!(well, why did I make this protection...)')
	exit()
