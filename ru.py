import config

# Help
help           = '''Команды:
┌───┬─────────┬────────────────────────────┬───────────────────────────────────────────────────────────┐
│ № │ Команда │ Название                   │ Описание                                                  │
├───┼─────────┼────────────────────────────┼───────────────────────────────────────────────────────────┤
│ 1 │ start   │ Приветствие                │ Просто выводит приветствие.                               │
│   │         │                            │  ^ Выполняется автоматически после запуска бота.          │
│ 2 │ help    │ Список команд              │ Выводит этот список.                                      │
│ 3 │ dialog  │ Режим диалога              │ Функция с приколом.                                       │
│ 4 │ new     │ Команда нового функционала │ Выводит честные причины долгого выхода обновлений.        │
│ 5 │ news    │ Новости                    │ Новости бота, а точнее новые функции.                     │
│ 6 │ echo    │ Эхо-режим                  │ Просто выводит то, что ты пишешь.                         │
│   │         │                            │  ^ Осторожно! Выйти от туда немного затруднительно.       │
│ 7 │ rand    │ Случайное число            │ Выводит рандомное число в вашем диапозоне.                │
│ 8 │ restart │ Перезапуск бота            │ Может использоваться для смены языка.                     │
│ 9 │ about   │ О PBot                     │ Выводит информацию о боте и авторе.                       │
└───┴─────────┴────────────────────────────┴───────────────────────────────────────────────────────────┘'''

# News
news           = '''Новости - (ААА?):
- Обновил список команд
- Добавил функцию перезапуска
- Добавил функцию "О PBot"
- Вопросы?'''

# About
about          = f'''
░▄▄▄▄░     ███░░███░░░░░░░░█░
▀▀▄██►     █░░█░█░░█░░██░░███
▀▀███►     ███░░███░░█░░█░░█░
░▀███►░█►  █░░░░█░░█░█░░█░░█░
▒▄████▀▀   █░░░░███░░░██░░░██

Бот написанный по домашнему заданию Алгоритмики.

{news}

{help}
'''

# Start
start          = f'Привет, меня зовут {config.Name}, бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши help'

# Tips
tip_exit       = 'Для выхода напиши "exit"'
tip_text       = 'Введите любой текст'

# Don't understand
du             = [
    'Что?',
    'Повтори',
    'Не понял',
    'Я тебя не понимаю',
    'Может напишешь help?',
    'Еще раз и я за тебя это сделаю',
    f'Ну всё\n\n{help}'
]

# Achivements
ach_mamont     = 'Мамонт заскамлен'
ach_received   = 'Вы получили достижение:'

# Dialog
dialog_welcome = 'Режим разговора. Тут ты можешь действительно поболтать о чем угодно. Чтобы выйти напиши "exit"'
dialog_rep1    = 'Хаха\nТы думал, я сюда ИИ запихал?'
dialog_rep2    = 'АХАХАХАХАХА'

# New
new_rep1       = 'Я сделяль новые функции, а это динозавр их сломал'
new_rep2       = 'Честно\n'
new_rep3       = 'Но я уже делаю новые со скоростью угашенной улитки!'

# Echo-mode
echomode_rep1  = '(Чтобы выйти напишите stop):'
echomode_rep2  = '(А волшебное слово):'
echomode_rep3  = '(Не расслышал):'
echomode_rep4  = '(А теперь всё вместе):'
echomode_exit  = 'Ну ладно, ладно. Не бугурти.'

# Rando
rando_rep1     = 'Минимальное число:'
rando_rep2     = 'Максимальное число:'

# Restart
restart        = 'Смена языка'

# Exit
exit           = 'Пока!'
