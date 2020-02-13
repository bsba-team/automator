from core import Bot
from templates import Template

template = Template()

class About:
    def about(self):
        @Bot.bot.message_handler(commands=['about'])
        def about(message):
            Bot.bot.reply_to(message, template.about(), parse_mode='HTML', disable_web_page_preview=True)
        pass
    pass
