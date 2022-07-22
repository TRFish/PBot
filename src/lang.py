langlist = '''
 ru - Russian
 en - English
'''

commands = ["start", "help", "dialog", "new", "news", "echo", "rand", "about"]

ru = {
    "cmd": {
        "head": {
            "cmd": "Команда",
            "cmds": "Команды",
            "name": "Название",
            "desc": "Описание",
        },
        "start": {
            "n": "Приветствие",
            "d": "Просто выводит приветствие. Выполняется автоматически после запуска бота."
        },
        "help": {
            "n": "Список команд",
            "d": "Выводит этот список."
        },
        "dialog": {
            "n": "Режим диалога",
            "d": "Функция с приколом."
        },
        "new": {
            "n": "Команда нового функционала",
            "d": "Выводит честные причины долгого выхода обновлений."
        },
        "news": {
            "n": "Новости",
            "d": "Новости бота, а точнее новые функции."
        },
        "echo": {
            "n": "Эхо-режим",
            "d": "Просто выводит то, что ты пишешь. Осторожно! Выйти от туда немного затруднительно."
        },
        "rand": {
            "n": "Случайное число",
            "d": "Выводит рандомное число в вашем диапозоне."
        },
        "about": {
            "n": "О PBot",
            "d": "Выводит информацию о боте и авторе."
        }
    },

    'news': '''Новости - (ААА?):
- Обновил список команд
- Добавил функцию перезапуска
- Добавил функцию "О PBot"
- Вопросы?''',

    'about': '''
░▄▄▄▄░     ███░░███░░░░░░░░█░
▀▀▄██►     █░░█░█░░█░░██░░███
▀▀███►     ███░░███░░█░░█░░█░
░▀███►░█►  █░░░░█░░█░█░░█░░█░
▒▄████▀▀   █░░░░███░░░██░░░██

Бот написанный по домашнему заданию Алгоритмики.''',

    'start': f'Привет, меня зовут PBot, бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши help',

    'tip': {
        'exit': 'Для выхода напиши "exit"',
        'text': 'Введите любой текст'
    },

    'du': [
        'Что?',
        'Повтори',
        'Не понял',
        'Я тебя не понимаю',
        'Может напишешь help?'
    ],

    'ach': {
        'mamont': 'Мамонт заскамлен',
        'received': 'Вы получили достижение:'
    },

    'dialog': {
        'welcome': 'Режим разговора. Тут ты можешь действительно поболтать о чем угодно. Чтобы выйти напиши "exit"',
        'rep1': 'Хаха\nТы думал, я сюда ИИ запихал?',
        'rep2': 'АХАХАХАХАХА'
    },

    'new': {
        'rep1': 'Я сделяль новые функции, а это динозавр их сломал',
        'rep2': 'Честно\n',
        'rep3': 'Но я уже делаю новые со скоростью угашенной улитки!'
    },

    'echomode': {
        'rep1': '(Чтобы выйти напишите stop):',
        'rep2': '(А волшебное слово):',
        'rep3': '(Не расслышал):',
        'rep4': '(А теперь всё вместе):',
        'exit': 'Ну ладно, ладно. Не бугурти.'
    },

    'rando': {
        'rep1': 'Минимальное число:',
        'rep2': 'Максимальное число:'
    },

    'restart': 'Смена языка',

    'exit': 'Пока!'
}

en = {
    "cmd": {
        "head": {
            "cmd": "Command",
            "cmds": "Commands",
            "name": "Name",
            "desc": "Description",
        },
        "start": {
            "n": "Greetings",
            "d": "It just prints out a greeting. In autostart."
        },
        "help": {
            "n": "Command List",
            "d": "Outputs this list."
        },
        "dialog": {
            "n": "Dialogue Mode",
            "d": "A tricky function."
        },
        "new": {
            "n": "New feature command",
            "d": "Displays honest reasons for the long release of updates."
        },
        "news": {
            "n": "News",
            "d": "Bot news, or rather new features."
        },
        "echo": {
            "n": "Echo-mode",
            "d": "It just prints what you write. Carefully! Getting out of there is a bit tricky."
        },
        "rand": {
            "n": "Ramdom number",
            "d": "Shows a random number in your range."
        },
        "about": {
            "n": "About PBot",
            "d": "Shows brief information about the project and the author."
        }
    },

    'news': '''News - (AAA?):
        - Updated the list of commands
        - Added restart function
        - Added "About PBot" feature
        - Questions?''',

    'about': '''
        ░▄▄▄▄░     ███░░███░░░░░░░░█░
        ▀▀▄██►     █░░█░█░░█░░██░░███
        ▀▀███►     ███░░███░░█░░█░░█░
        ░▀███►░█►  █░░░░█░░█░█░░█░░█░
        ▒▄████▀▀   █░░░░███░░░██░░░██
        
        Bot written according to the homework of the Algorithmika school.''',
    
    'start': f'Hi, my name is PBot, a bot for all occasions (well, or for those provided by the code)\nTo display a list of commands, write help',

    'tip': {
        'exit': 'To exit, write "exit"',
        'text': 'Enter any text'
    },

    'du': [
        'What?',
        'Repeat',
        'Not understood',
        "I don't understand you",
        'Can you write help?'
    ],

    'ach': {
        'mamont': 'The mammoth is deceived',
        'received': 'You have received an achievement:'
    },

    'dialog': {
        'welcome': 'Dialog-mode. Here you can really chat about anything. {tip_exit}',
        'rep1': 'Hahaha\nDid you think I put it in here?',
        'rep2': 'HAHAHAHAHAHAHA'
    },

    'new': {
        'rep1': 'I made new functions, and this dinosaur broke them',
        'rep2': 'Honestly\n',
        'rep3': "But I'm already making new ones at the speed of a dead snail!"
    },

    'echomode': {
        'rep1': '(To exit, write "stop"):',
        'rep2': '(And the magic word):',
        'rep3': "(I didn't hear you):",
        'rep4': '(And now all together):',
        'exit': "All right, all right. Don't shout."
    },

    'rando': {
        'rep1': 'Minimum number:',
        'rep2': 'Maximum number:'
    },

    'restart': 'Switch language',

    'exit': 'Bye!'
}
