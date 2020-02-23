import telebot
import config
import os
from core import Logs

class Bot:
    if config.DEBUG:
        bot = telebot.TeleBot(config.TOKEN)
    else:
        bot = telebot.TeleBot(os.getenv("TOKEN"))


    def start(self):
        logs = Logs()
        logs.log()
        Bot.bot.polling(none_stop=True, interval=0)
        pass
    pass
