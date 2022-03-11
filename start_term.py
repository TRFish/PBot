#!/bin/python
from backend import *
command = 'start'
while command != 'exit':
	input_analyzer(command)
	command = input('>> ')