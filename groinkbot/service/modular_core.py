import re
import functools
import time
import random as rd


def link(bot):
    print(f"Bot commands linked to {bot}")

def unlink(bot):
    print(f"Bot commands unlinked from {bot}")


# "\A" = "starts with"
call = r"\Ahey bot "
pref = r"\A!"

#### Utils ####
def hello():
    l = ["Hello", "Hi", "Hey"]
    return rd.choice(l)

def join():
    return ""
    return f"{hello()} there luciWave"


#### Commands management ####

class BluePrint:
    def __init__(self):
        # Start with !
        self.pref_commands = {}

        # Starts with "hey bot"
        self.call_commands = {}

        # No special format
        self.text_commands = {}

    def __call__(self, min_auth, commands, name=None):
        def inside(func):
            # Wrap
            @functools.wraps(func)
            def wrapper(bot, msg, user):
                if user.lowername == name:
                    return func(bot, msg, user)
                elif user.rights >= min_auth and name is None:
                    return func(bot, msg, user)

            # Add commands to the dict
            for c in commands:
                if c.startswith(pref):
                    self.pref_commands[c]=wrapper
                elif c.startswith(call):
                    self.call_commands[c]=wrapper
                else:
                    self.text_commands[c]=wrapper
            return wrapper
        return inside

    def add_commands_batch(self, commands):
        self.pref_commands = {**self.pref_commands, **commands}

#### Bot management ####

auth = BluePrint()

@auth(2, [pref+"ignore"])
def f(bot, msg, user):
    pass # Ignore the triggers in the message

@auth(2, ["go sleep bot", "bye bot", pref+"sleep"])
def f(bot, msg, user):
    bot.send_message("Bye!")
    bot.stop()

@auth(2, [call+"reload", pref+"reload"])
def f(bot, msg, user):
    bot.reload()

@auth(2, [call + "load module ", call + "load modules "])
def f(bot, msg, user):
    l = msg.split(" ")
    bot.add_modules(l)
    print("Loaded modules:", l)

@auth(2, [call + "forget module ", call + "forget modules "])
def f(bot, msg, user):
    l = msg.split(" ")
    bot.remove_modules(l)
    print("Forgotten modules:", l)


#### Commands ####

@auth(0, ["hi bot", "hello bot", "hey bot\Z", "hey bot!", "hey groinkbot", "hi groinkbot", "hello groinkbot"])
def f(bot, msg, user):
    if user.rights == 0:
        bot.send_message(f"{hello()} {user.name} luciWave")
    elif user.rights == 1:
        bot.send_message(f"Oh {hello()} {user.name} peepoClap")
    elif user.rights == 2:
        bot.send_message(f"{user.name} widepeepoHappy")
    elif user.rights == 3:
        bot.send_message(f"Hi Master luciHeart")

@auth(0, [call + "how do you work", call + "who are you"])
def f(bot, msg, user):
    m = "Hi, I'm GroinkBot v2 peepoClap I'm coded in Python 3.7, running headless on a Raspberry Pi 4. "
    m += "Messages are processed with regular expressions mapping to custom functions, which execute commands. "
    m += "My code is not open source yet, but it might be in the future luciLurk"
    bot.send_message(m)
