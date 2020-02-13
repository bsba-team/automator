from core import Bot
from templates import Template

template = Template()

class Error:
    def error(self):
        @Bot.bot.message_handler(func=lambda message: True, content_types=['text'])
        def error(message):
            Bot.bot.send_message(message.chat.id, template.error(), parse_mode='HTML', disable_web_page_preview=True)
        pass
    pass