import logging
import telebot
from core.Custom import Colors


# Outputs debug messages to console.
class Logs:
    def log(self):
        print(
            Colors.BOLD + Colors.RED + "Check phase of bot completed! Bot is working..." + Colors.END)
        print(
            Colors.BOLD + Colors.YELLOW + "For any further problems or bugs," + Colors.END)
        print(
            Colors.BOLD + Colors.YELLOW + "Please, contact with the creator:" + Colors.END)
        print(Colors.BOLD + Colors.RED + "https://t.me/sakhib_orzklv" + Colors.END)
        telebot.logger.setLevel(logging.DEBUG)
    pass
