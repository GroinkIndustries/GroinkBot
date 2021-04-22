import importlib

class Bot:
    def __init__(self):
        self.interface = None

    def __repr__(self):
        r = f"<Bot | {__repr__(self.interface)}>"
        return r

    def reload(self):
        self.interface.reload()
        print("Reloaded")

    def on_welcome(self):
        self.send_message = self.interface.send_message
        self.send_message("Hello world")

    def get_message(self, message, user):
        print(f"{user.username} > {message}")
        if user.rights==1:
            self.send_message(f"Mod o7: {message}")
        elif user.rights==2:
            self.send_message(f"\o/ Owner \o/: {message}")
        else:
            self.send_message(f"I got the message: {message}")

    def stop(self):
        print("Stopping", self)
        self.interface.stop()

    def start(self):
        self.interface.start()
