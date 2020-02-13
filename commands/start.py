from core import Bot
from data import User
from data import Step
from templates import Template

users = User()
steps = Step
template = Template()

class Start:
    def start(self):
        @Bot.bot.message_handler(commands=['start'])
        def start(message):
            Bot.bot.reply_to(message, template.start(), parse_mode='HTML', disable_web_page_preview=True)
            mid = message.chat.id
            if mid not in users.users:  # if user hasn't used the "/start" command yet:
                users.users.append(mid)  # save user id, so you could broadcast messages to all users of this bot later
                steps.steps[mid] = 0  # save user id and his current "command level", so he can use the "/getImage"
                Bot.bot.send_message(mid, '<b>Hello, stranger, let me scan you...</b>', parse_mode='HTML', disable_web_page_preview=True)
                Bot.bot.send_message(mid, '<b>Scanning complete, I know you now</b>', parse_mode='HTML', disable_web_page_preview=True)
                Bot.bot.send_message(mid, '<b>Let\'s get started!</b>', parse_mode='HTML', disable_web_page_preview=True)
                Bot.bot.send_message(mid, template.help(), parse_mode='HTML', disable_web_page_preview=True)
            else:
                Bot.bot.send_message(mid, '<b>I already know you, no need for me to scan you again! Btw, you can use</b> /help <b>to get menu...</b>', parse_mode='HTML', disable_web_page_preview=True)
        pass
    pass
