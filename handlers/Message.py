from core import Bot
from templates import Template

template = Template()

class Message:
    def message(self):
        @Bot.bot.message_handler(content_types=['text'])
        def text_message(message):
            if message.text == "/start":
                Bot.bot.reply_to(message, template.start(), parse_mode='HTML', disable_web_page_preview=True)
            elif message.text == "/help":
                Bot.bot.reply_to(message, template.help(), parse_mode='HTML', disable_web_page_preview=True)
            elif message.text == "/about":
                Bot.bot.reply_to(message, template.about(), parse_mode='HTML', disable_web_page_preview=True)
            else:
                Bot.bot.reply_to(message, template.error(), parse_mode='HTML', disable_web_page_preview=True)
            pass
        pass
    pass
