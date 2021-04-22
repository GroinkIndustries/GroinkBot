import json
import sys
from irc.bot import SingleServerIRCBot, ReconnectStrategy
from requests import get
import threading

from .cli_interface import Interface, User

class No_Reconnect(ReconnectStrategy):
    def __init__(self, **attrs):
        pass

    def run(self, bot):
        print("Not reconnecting to", bot)
        return

class Twitch(SingleServerIRCBot, Interface):
    def __init__(self, auth, roles, service, channel=None, running=lambda:True):
        self.running = running
        self.service = None
        Interface.__init__(self, service)
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667

        if not channel.startswith("#"):
            channel = f"#{channel}"
        self.CHANNEL = channel

        self.CLIENT_ID = auth["client_id"]
        self.TOKEN = auth["token"]
        self.USERNAME = auth["username"]
        
        self.ROLES = roles

        url = f"https://api.twitch.tv/kraken/users?login={self.USERNAME}"
        headers = {"Client-ID": self.CLIENT_ID, "Accept": "application/vnd.twitchtv.v5+json"}
        resp = get(url, headers=headers).json()
        self.channel_id = resp["users"][0]["_id"]

        SingleServerIRCBot.__init__(self, [(self.HOST, self.PORT, f"oauth:{self.TOKEN}")],
            self.USERNAME, self.USERNAME, recon=No_Reconnect())

    def __repr__(self):
        r = f"<Twitch chat | {self.CHANNEL}>"
        return r

    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.CHANNEL)
        self.service.on_welcome()
        print(f"Chat joined: {self.CHANNEL}")

    def get_role(self, username):
        u = username.lower()
        for k, v in self.ROLES.items():
            if k == u:
                return v
        return 0

    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        uname = tags["display-name"]
        message = event.arguments[0]
        urights = self.get_role(uname)

        user = User(uname, uname.lower(), urights)

        print(f"{message}")

        self.service.get_message(message, user)

    def send_message(self, message):
        print(f"> {message}")
        self.connection.privmsg(self.CHANNEL, message)

    def stop(self):
        self.running = lambda:False
        # self.die()
        # sys.exit(0)

    def start(self):
        self._connect()
        print("Entering listen loop")
        while self.running():
            self.reactor.process_once(0.2)
        self.reactor.disconnect_all()
        print("Exited listen loop")

    def reload(self):
        self.get_params()
        print("Interface reloaded")
