from commands import Start
from commands import Help

class Handler:
    def handler(self):

        # Start command
        start = Start()
        start.start()

        # Help command
        help = Help()
        help.help()

    pass
