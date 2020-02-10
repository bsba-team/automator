import telebot
import config
from core import Logs

class Bot:
    bot = telebot.TeleBot(config.TOKEN)

    def start(self):
        logs = Logs()
        logs.log()
        Bot.bot.polling(none_stop=True, interval=0)
        pass
    pass
