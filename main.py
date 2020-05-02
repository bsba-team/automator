# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from . import config


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    pass


try:
    print('Importing "pyTelegramBotApi"...')
    import telebot
    print('Successfully imported "pyTelegramBotApi"')

    print('Bot has started...')
except ImportError as err:
    install("pyTelegramBotApi")
    os.execl(sys.executable, sys.executable, *sys.argv)


bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
