import telegram
import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
print('Telegram bot is running')

BOT_TOKEN = '978274934:AAHR-ZIEXsphxpKEbDUVpk-XAeK78I6ATEc'
BOT_NAME = 'BSBA™: Main Bot'
BOT_USERNAME = 'bsba_bot'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


def stop(updater):
    updater.stop()


updater.start_polling()
