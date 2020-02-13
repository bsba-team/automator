from commands import Start
from commands import Help
from commands import About

class Handler:
    def handler(self):

        # Start command
        start = Start()
        start.start()

        # Help command
        help = Help()
        help.help()

        # About command
        about = About()
        about.about()
    pass
