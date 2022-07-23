#!/usr/bin/env python3
####  ####        #    ▄▄▄▄
#   # #   #  ##  ###  ▀▀▄██►
####  ####  #  #  #   ▀▀███►
#     #   # #  #  #    ▀███► █►
#     ####   ##   ##   ▄████▀▀

import random
import time
import argparse
import yaml
from rich.console import Console
from rich.table import Table


class PBot():
	def __init__(self):
		self.console = Console()
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
				self.echoMode()
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
		print(f'{config["images"]["dino"]}\n{text["new"]["rep1"]}')
		time.sleep(0.1)
		print(text['new']['rep2'])
		time.sleep(4)
		print(f'{config["images"]["snail"]}\n{text["new"]["rep3"]}')
	
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
		self.table = Table(title=text["cmd"]["name"])
		
		self.table.add_column("#", style="cyan", no_wrap=True)
		self.table.add_column(text["cmd"]["head"]["cmd"], style="magenta")
		self.table.add_column(text["cmd"]["head"]["name"], style="green")
		self.table.add_column(text["cmd"]["head"]["desc"])
		
		for i in range(len(config["commands"])):
			self.table.add_row(str(i+1), config['commands'][i], text["cmd"][config["commands"][i]][0], text["cmd"][config["commands"][i]][1])
		
		self.console.print(self.table)
	
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
		langtext = ''
		for i in config["langlist"]:
			langtext += f'\n {i["id"]} - {i["name"]}'
		print(f'Choose language: {langtext}')
		lng = input(config["pointer"]["style"]) or 'ru'
	
	with open(f'langs/{lng}.yml', encoding="utf8") as h:
		return yaml.safe_load(h)

def main():
	bot = PBot()
	command = 'start'
	# Shell loop
	while command != 'exit':
		bot.analyzer(command)
		command = input(config["pointer"]["style"])

if __name__ == '__main__':
	with open('configs/config.yml', encoding="utf8") as f:
		config = yaml.safe_load(f)
	
	text = langChooser(argumentsParser().lang)
	main()
