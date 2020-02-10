import logging
import telebot
import customization


# Outputs debug messages to console.
def bot_logs():
    logger = telebot.logger
    print(customization.color.BOLD + customization.color.RED + "Check phase of bot completed! Bot is working..." + customization.color.END)
    print(customization.color.BOLD + customization.color.YELLOW + "For any further problems or bugs," + customization.color.END)
    print(customization.color.BOLD + customization.color.YELLOW + "Please, contact with the creator:" + customization.color.END)
    print(customization.color.BOLD + customization.color.RED + "https://t.me/sakhib_orzklv" + customization.color.END)
    telebot.logger.setLevel(logging.DEBUG)
