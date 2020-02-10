import logging
import telebot
import customization


# Outputs debug messages to console.
def bot_logs():
    logger = telebot.logger
    print(customization.color.BOLD + customization.color.RED + "Bot started working" + customization.color.END)
    telebot.logger.setLevel(logging.DEBUG)
