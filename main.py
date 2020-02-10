from core.Bot import Bot
from handlers import HandleMessage

# Message handler
message_handler = HandleMessage()
message_handler.message()

# Bot starter
bot = Bot()
bot.start()
