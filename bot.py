#!/bin/python
import config
import telebot
from token import *
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Привет, меня зовут ' + config.Name + ', бот на все случаи жизни(ну или на те что предусмотрены кодом)\nЧтобы вывести список команд напиши /help')

@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Список команд пока не доступен')

@bot.message_handler(commands=["new"])
def new(m, res=False):
    bot.send_message(m.chat.id, '░▄▄▄▄░\n▀▀▄██►\n▀▀███►\n░▀███►░█►\n▒▄████▀▀\n\nЯ сделяль новые функции, а это динозавр их сломал')
    time.sleep(0.1)
    bot.send_message(m.chat.id, 'Честно')
    time.sleep(4)
    bot.send_message(m.chat.id, '───▄▄▄\n─▄▀░▄░▀▄\n─█░█▄▀░█\n─█░▀▄▄▀█▄█▄▀\n▄▄█▄▄▄▄███▀\nНо я уже делаю новые со скоростью угашенной улитки!')

@bot.message_handler(commands=["news"])
def news(m, res=False):
    bot.send_message(m.chat.id, 'Новое в Боте:\n- _|__|_ \|Ничего|/ _|__|_ (Всё что не относится к другим командам):\nПо заголовку вы могли понять, что я ничего не добавил, но _|__|_ \|Ничего|/ _|__|_ это новая команда, которая выводит _|__|_ \|НИЧЕГО|/ _|__|_ !\nИ самое важное в этой команде она в добавок ко всему ничего не делает!\n- Команда нового функционала (/new)\nВыводит честные причины долгого выхода обговлений.\n- Echo-mode (/echo)\nПросто выводит то, что ты пишешь\nОсторожно! Выйти от туда немного затруднительно.')


bot.polling(none_stop=True, interval=0)
