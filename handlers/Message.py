from core import Bot

class HandleMessage:
    def message(self):
        bot = Bot()
        bot.bot()

        @bot.message_handler(content_types=['text'])
        def text_message(message):
            if message.text == "/start":
                bot.reply_to(message, "Message", parse_mode='HTML', disable_web_page_preview=True)
            elif message.text == "/help":
                bot.reply_to(message, "Message", parse_mode='HTML', disable_web_page_preview=True)
            else:
                bot.reply_to(message, "Message", parse_mode='HTML', disable_web_page_preview=True)
            pass
        pass
    pass
