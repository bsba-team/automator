import config
import telebot
import logger
import messages.message



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == "/start":
        bot.reply_to(message, messages.message.start, parse_mode='HTML')
    else:
        bot.reply_to(message, '<b>Please, can you type<b> /help. I can\'t get you')

logger.bot_logs()
bot.polling(none_stop=True, interval=0)