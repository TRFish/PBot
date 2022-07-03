#!/usr/bin/env python3
#####  ####           ##    ▄▄▄▄
#    # #   #   ###   ####  ▀▀▄██►
#####  ####  ##   ##  ##   ▀▀███►
#      #   # ##   ##  ##    ▀███► █►
#      ####    ###    ###   ▄████▀▀

import random
import sys
import time
import config
import image


class PBot():
	def __init__(self):
		self.du_i = 0

	def input_analyzer(self, command):
		command = command.lower()
		match command:
			case 'start':
				self.start()
			case 'help':
				self.help()
			case 'dialog':
				self.dialog()
			case 'new':
				self.new()
			case 'news':
				self.news()
			case 'echo':
				self.echo_mode()
			case 'rand':
				self.rando()
			case 'random':
				self.rando()
			case 'about':
				self.about()
			case _:
				self.du()

	# Don't understand
	def du(self):
		print(text.du[self.du_i])
		if self.du_i < len(text.du) - 1:
			self.du_i += 1
		else:
			self.du_i = 0

	# Talk
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

	# New functionality, or rather why it does not come out
	def new(self):
		print(f'{image.dino}\n{text.new_rep1}')
		time.sleep(0.1)
		print(text.new_rep2)
		time.sleep(4)
		print(f'{image.snail}\n{text.new_rep3}')

	# Echo
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

	# Random
	def rando(self):
		self.minimal = int(input(text.rando_rep1))
		self.maximal = int(input(text.rando_rep2))
		self.output  = random.randint(self.minimal, self.maximal)
		print(self.output)

	# Bot news
	def news(self):
		print(text.news)

	# Command table
	def help(self):
		print(text.help)

	# Welcome_text
	def start(self):
		print(text.start)

	# About
	def about(self):
		print(text.about)


if __name__ == '__main__':
	running = True

# Main loop
while running:
	arg = sys.argv
	if len(arg) == 1:
		arg.append(None)
	lng = arg[1]

	# Lang chooser
	if lng is not None:
		text = __import__(lng)
	elif config.lang is not None:
		text = __import__(config.lang)
	else:
		lng = input(f'Choose language:\n ru - Russian\n en - English\n(ru) {config.Pointer}')
		if lng == '':
			lng = 'ru'
		text = __import__(lng)

	bot = PBot()
	command = 'start'
	# Shell loop
	while command != 'exit' and command != 'restart':
		bot.input_analyzer(command)
		command = input(f'{config.Prefix}{config.Pointer}')
	
	# Exit or restart?
	if command == 'exit':
		print(text.exit)
		running = False
	elif command == 'restart':
		print(text.restart, '\n\n')
