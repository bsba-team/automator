from core.Bot import Bot
from templates import Message

class Message:
    def message(self):
        @Bot.bot.message_handler(content_types=['text'])
        def text_message(message):
            if message.text == "/start":
                Bot.bot.reply_to(message, "Message", parse_mode='HTML', disable_web_page_preview=True)
            elif message.text == "/help":
                Bot.bot.reply_to(message, "Message", parse_mode='HTML', disable_web_page_preview=True)
            else:
                Bot.bot.reply_to(message, "Message", parse_mode='HTML', disable_web_page_preview=True)
            pass

        pass
        pass
    pass
