# -*- coding: utf-8 -*-

try:
    print('Importing "time"...')
    import time

    print('Successfully imported "time"')

    print('Importing "pyTelegramBotApi"...')
    import telebot

    print('Successfully imported "pyTelegramBotApi"')

    print('Importing "configs"...')
    import config

    print('Successfully imported "config"')

    print('Bot has started...')
except ImportError:
    print('Failed to import required modules, quitting...')
    exit(1)

bot = telebot.TeleBot(token=config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
