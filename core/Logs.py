import logging
import telebot
from core import Custom


# Outputs debug messages to console.
class Logs:
    def log(self):
        print(
            Custom.Colors.BOLD + Custom.Colors.RED + "Check phase of bot completed! Bot is working..." + Custom.Colors.END)
        print(
            Custom.Colors.BOLD + Custom.Colors.YELLOW + "For any further problems or bugs," + Custom.Colors.END)
        print(
            Custom.Colors.BOLD + Custom.Colors.YELLOW + "Please, contact with the creator:" + Custom.Colors.END)
        print(Custom.Colors.BOLD + Custom.Colors.RED + "https://t.me/sakhib_orzklv" + Custom.Colors.END)
        telebot.logger.setLevel(logging.DEBUG)
    pass
