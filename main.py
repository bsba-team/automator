from core import Bot

# bot = telebot.TeleBot(config.TOKEN)
#
# @bot.message_handler(content_types=['text'])
# def text_message(message):
#     if message.text == "/start":
#         bot.reply_to(message, messages.message.start, parse_mode='HTML', disable_web_page_preview=True)
#     elif message.text == "/help":
#         bot.reply_to(message, messages.message.help, parse_mode='HTML', disable_web_page_preview=True)
#     else:
#         bot.reply_to(message, messages.message.error, parse_mode='HTML', disable_web_page_preview=True)

# Bot
bot = Bot()
bot.start()

# bot.polling(none_stop=True, interval=0)