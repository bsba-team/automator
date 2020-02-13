from core import Bot
from templates import Template

template = Template()

class Help:
    def help(self):
        @Bot.bot.message_handler(commands=['help'])
        def help(message):
            Bot.bot.reply_to(message, template.help(), parse_mode='HTML', disable_web_page_preview=True)
        pass
    pass
