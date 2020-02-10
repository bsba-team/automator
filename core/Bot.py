import telebot
import config
from core import Logs

class Bot:
    def start(self):
        logs = Logs()
        logs.log()
        bot = telebot.TeleBot(config.TOKEN)
        bot.polling(none_stop=True, interval=0)
        pass
    pass
