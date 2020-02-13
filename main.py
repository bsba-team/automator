from core import Bot
from handlers import Handler

# Message handler
message_handler = Handler()
message_handler.handler()

# Bot starter
bot = Bot()
bot.start()
