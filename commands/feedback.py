from core import Bot
from templates import Template
from config import ADMIN_CHATID

template = Template()


class Feedback:
    def feedback(self):
        @Bot.bot.message_handler(commands=['feedback'])
        def feedback(message):
            Bot.bot.reply_to(message, template.feedback(), parse_mode='HTML', disable_web_page_preview=True)
            Bot.bot.send_message(ADMIN_CHATID, "From: " + message.chat.username + "\n" +
                                 "Feedback: " + message.text,
                                 parse_mode='HTML', disable_notification=True, disable_web_page_preview=True)

        pass

    pass
