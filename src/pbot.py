#!/usr/bin/env python3
####  ####        #    ▄▄▄▄
#   # #   #  ##  ###  ▀▀▄██►
####  ####  #  #  #   ▀▀███►
#     #   # #  #  #    ▀███► █►
#     ####   ##   ##   ▄████▀▀

import random
import time
import image
import lang
import argparse
import yaml


class PBot():
	def __init__(self):
		self.du_i = 0
	
	# Simple input analyzer
	def analyzer(self, command):
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
			case 'rand' | 'random':
				self.rando()
			case 'about':
				self.about()
			case _:
				self.du()
	
	# Don't understand
	def du(self):
		print(text['du'][self.du_i])
		if self.du_i < len(text['du']) - 1:
			self.du_i += 1
		else:
			self.du_i = 0
	
	# Talk
	def dialog(self):
		print(text['dialog']['welcome'])
		self.text = input('>> ')
		while self.text != 'exit':
			#Достижение(Скам мамонта №1)
			if config.A_Mamont_V == 0:
				print(text['dialog']['rep1'])
				print(text['ach']['received'], text['ach']['mamont'])
				config.A_Mamont_V = 1
				print(text['dialog']['rep2'])
			self.text = input(f'\n{text["tip"]["exit"]}:\n')
		del self.text
	
	# New functionality, or rather why it does not come out
	def new(self):
		print(f'{image.dino}\n{text["new"]["rep1"]}')
		time.sleep(0.1)
		print(text['new']['rep2'])
		time.sleep(4)
		print(f'{image.snail}\n{text["new"]["rep3"]}')
	
	# Echo
	def echoMode(self):
		self.text = None
		while self.text != 'Stop. Please, stop!':
			while self.text != 'Please!':
				while self.text != 'please':
					while self.text != 'stop':
						self.text = input(f'{text["tip"]["text"]} {text["echomode"]["rep1"]}')
						print(self.text)
					self.text = input(f'{text["tip"]["text"]} {text["echomode"]["rep2"]}')
					print(self.text)
				self.text = input(f'{text["tip"]["text"]} {text["echomode"]["rep3"]}')
				print(self.text)
			self.text = input(f'{text["tip"]["text"]} {text["echomode"]["rep4"]}')
			print(self.text)
		del self.text
		print(text['echomode']['exit'])
	
	# Random
	def rando(self):
		self.minimal = int(input(text['rando']['rep1']))
		self.maximal = int(input(text['rando']['rep2']))
		self.output  = random.randint(self.minimal, self.maximal)
		print(self.output)
	
	# Bot news
	def news(self):
		print(text['news'])
	
	# Command table
	def help(self):
		print(text['help'])
	
	# Welcome_text
	def start(self):
		print(text['start'])
	
	# About
	def about(self):
		print(text['about'])

def argumentsParser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-l', '--lang', nargs='*', help='Set language')
	return parser.parse_args()

def langChooser(arg):
	if arg is not None:
		lng = arg
	elif config['lang'] is not None:
		lng = config['lang']
	else:
		lng = input(f'Choose language:{lang.langlist}(ru) {config["pointer"]["style"]}')
	
	match(lng):
		case 'ru':
			text = lang.ru
		case 'en':
			text = lang.en
		case _: 
			text = lang.ru
	
	return text

def main():
	bot = PBot()
	command = 'start'
	# Shell loop
	while command != 'exit' and command != 'restart':
		bot.analyzer(command)
		command = input(config["pointer"]["style"])

if __name__ == '__main__':
	with open('../configs/config.yml') as f:
		config = yaml.safe_load(f)
	
	text = langChooser(argumentsParser().lang)
	main()
