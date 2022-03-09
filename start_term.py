#!/bin/python

from backend import *

# Еще один безполезный комент объясняющий смысл и так понятного куска кода
command = 'start'
while command != 'exit':
	input_analyzer(command)
	command = input('\n>> ')
