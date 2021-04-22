import sys
from collections import namedtuple
User = namedtuple('User', 'name lowername rights')

class Interface:
    def __init__(self, service):
        self.service = service
        service.interface = self

    def __repr__(self):
        r = "<Interface>"
        return r

    def on_welcome(self):
        self.service.on_welcome()

    def get_message(self, message, username):
        u = User(username, username.lower(), 2)
        self.service.get_message(message, u)

    def stop(self):
        sys.exit(0)

    def reload(self):
        print("Interface reloaded")

class CLIInterface(Interface):
    def __init__(self, service, name="Me"):
        self.name=name
        Interface.__init__(self, service)

    def __repr__(self):
        r = "<CLI Interface>"
        return r

    def send_message(self, message):
        print(f"> {message}")

    def start(self):
        self.on_welcome()
        print("Starting input loop\n")
        while True:
            message = input()
            if message == "end":
                self.stop()
            self.get_message(message, self.name)
