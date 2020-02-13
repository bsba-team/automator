from core import Bot
from templates import Template

template = Template()

class Start:
    def start(self):
        @Bot.bot.message_handler(commands=['start'])
        def start(message):
            Bot.bot.reply_to(message, template.start(), parse_mode='HTML', disable_web_page_preview=True)
        pass
    pass
