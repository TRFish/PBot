import config

# Выбор языка
while config.Lang == '':
	lang = input('Выберите язык:\n 1 - ru_RU | Русский\n 2 - en_US\nChoose: ')
	if lang == '2':
		from lang.en_US import *
		break
	else:
		from lang.ru_RU import *
		break

if config.Lang == 'ru_RU':
	from lang.ru_RU import *
elif config.Lang == 'en_US':
	from lang.en_US import *