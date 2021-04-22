import discord as discordlib
from .cli_interface import *

import asyncio
import logging
import signal
import sys
import traceback
log = logging.getLogger(__name__)

def get_elt(list, name):
    for e in list:
        if e.name == name:
            return e
    return None

class Discord(discordlib.Client, Interface):
    def __init__(self, auth, roles, service, guild, running=lambda:True):
        discordlib.Client.__init__(self)
        self.running = running
        self.service = None
        Interface.__init__(self, service)
        
        self.ROLES = roles
        self.TOKEN = auth["token"]
        self.guild_name = auth["guild"]
        self.default_channel = auth["channel"]
        self.channel = None

        self.service.send_message = self.send_message

    def __repr__(self):
        r = "<CLI Interface>"
        return r

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        g = get_elt(self.guilds, self.guild_name)
        self.channel = get_elt(g.channels, self.channel)

    def get_role(self, username):
        u = username.lower()
        for k, v in self.ROLES.items():
            if k == u:
                return v
        return 0

    async def on_message(self, message):
        if message.author == self.user:
            return
        urights = self.get_role(str(message.author))
        uname = f"<@{str(message.author.id)}>"
        user = User(uname, str(message.author).lower(), urights)

        self.channel = message.channel
        msg = message.content

        print(f"{uname} ({urights}): {msg}")

        self.service.get_message(msg, user)

        # if msg.lower() == "hi bot":
        #     await self.send_message("Hi Master")
        #     return

        # if msg.lower() == "bye bot":
        #     self.stop()

    def send_message(self, message):
        asyncio.ensure_future(self.channel.send(message))
        print(f"> {message}")

    def start(self):
        self.run()
        self.service.on_welcome()
        self.on_welcome()
        self.send_message("Hello World")
        print("Starting input loop\n")

    def run(self):
        loop = self.loop

        try:
            loop.add_signal_handler(signal.SIGINT, lambda: loop.stop())
            loop.add_signal_handler(signal.SIGTERM, lambda: loop.stop())
        except NotImplementedError:
            pass

        async def runner():
            try:
                await self.login(self.TOKEN)
                await self.connect()
            finally:
                if not self.is_closed():
                    await self.close()

        def stop_loop_on_completion(f):
            loop.stop()

        future = asyncio.ensure_future(runner(), loop=loop)
        future.add_done_callback(stop_loop_on_completion)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            log.info('Received signal to terminate bot and event loop.')
        finally:
            future.remove_done_callback(stop_loop_on_completion)
            log.info('Cleaning up tasks.')
            self.stop()
        if not future.cancelled():
            try:
                return future.result()
            except KeyboardInterrupt:
                # I am unsure why this gets raised here but suppress it anyway
                return None


    def stop(self):
        self.running = lambda:False
        self.loop.stop()

