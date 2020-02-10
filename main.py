import config
import telebot
import logging
import customization

bot = telebot.TeleBot(config.TOKEN)
logger = telebot.logger
print(customization.color.BOLD + customization.color.RED + "Bot started working" + customization.color.END)


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text == "/start":
        bot.reply_to(message, '<b>So this is my brand new message</b>', parse_mode='HTML')
    else:
        bot.reply_to(message, '<b>Please, can you type<b> /help. I can\'t get you')


telebot.logger.setLevel(logging.DEBUG) # Outputs debug messages to console.
bot.polling(none_stop=True, interval=0)