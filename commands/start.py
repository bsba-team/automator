from core import Bot
from telebot.types import Message
from templates import Template

class Start:
    def start(self, message: Message):
        @Bot.bot.message_handler(content_types=['text'])
        def text_message(message):
            if message.text == "/start":
                Bot.bot.reply_to(message, template.start(), parse_mode='HTML', disable_web_page_preview=True)
            elif message.text == "/help":
                Bot.bot.reply._to(message, template.help(), parse_mode='HTML', disable_web_page_preview=True)
            else:
                Bot.bot.reply_to(message, template.error(), parse_mode='HTML', disable_web_page_preview=True)
            pass

        pass