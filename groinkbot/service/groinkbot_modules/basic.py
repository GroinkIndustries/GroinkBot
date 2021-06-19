from ..modular_core import call, pref, BluePrint, rd, time, hello
auth = BluePrint()

def link(bot):
    print(f"GroinkBot connected")

def unlink(bot):
    print(f"GroinkBot disconnected")


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
        bot.send_message("Hey nerds, I'm back peepoClap")
        # bot.send_message(f"Hi Master luciHeart")

@auth(0, ["good bot", "best bot", "thanks bot", "thank you bot"])
def f(bot, msg, user):
    bot.send_message("peepoClap")

@auth(0, [call + "how do you work", call + "who are you", pref + "groinkbot"])
def f(bot, msg, user):
    m = "Hi, I'm GroinkBot v2 peepoClap I'm coded in Python 3.7, running headless on a Raspberry Pi 4. "
    m += "Messages are processed with regular expressions mapping to custom functions, which execute commands. "
    m += "My code is not open source yet, but it might be in the future luciLurk"
    bot.send_message(m)

@auth(0, [call + "who am i"])
def f(bot, msg, user):
    m = f"Hi {user.name}, for my systems you are "
    if user.rights == 0:
        m += "a plebs luciLurk"
    elif user.rights == 1:
        m += "an customized user luciHeart"
    elif user.rights == 2:
        m += "an admin luciSalute"
    elif user.rights == 3:
        m += "My Master peepoClap"
    bot.send_message(m)

@auth(2, [call + "test"])
def f(bot, msg, user):
    bot.send_message(msg)