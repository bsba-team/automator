from commands import Start
from commands import Help
from commands import About
from commands import Error

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

        # Error command
        error = Error()
        error.error()
    pass
