class Template:
    def start(self):
        start = open('templates/template/start.html', 'rb').read()
        return start
        pass
    pass

    def help(self):
        help = open('templates/template/help.html', 'rb').read()
        return help
        pass
    pass

    def error(self):
        error = open('templates/template/error.html', 'rb').read()
        return error
        pass
    pass
