# -*- coding: utf-8 -*-

try:
    print('Importing "time"...')
    import time
    print('Successfully imported "time"')
    print('Importing "pyTelegramBotApi"...')
    import telebot
    print('Successfully imported "pyTelegramBotApi"')
except ImportError:
    print('Failed to import required modules, quitting...')
    exit(1)

BOT_TOKEN = ''

bot = telebot.TeleBot(token=BOT_TOKEN)