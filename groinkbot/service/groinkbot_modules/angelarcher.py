from ..modular_core import call, pref, BluePrint, rd, time, hello
auth = BluePrint()

def link(bot):
    print(f"GroinkBot connected")

def unlink(bot):
    print(f"GroinkBot disconnected")

dc_link = "https://discord.gg/kGDcMGQ"

luci_pref_commands = {
    pref + "cheese":"CHEESE peepoFat",
    pref + "hydrate" : "luciSip sluuuuuurp luciSip",
    pref + "hiccup": "Wow that's a lot of hiccups luciDuffpog",
    pref + "vedi": "What a donut peepoFat",
    pref + "miky": "!meow Meow for Miky, bot peepoClap",
    pref + "sub" : "luciHeart Thanks Luci for the sub luciShy",
    pref + "hipo" : "!hiccup luciDuffpog",
    pref + "nunobot": "BEEP BOOP He's my cousin peepoClap BEEP BOOP",
    pref + "gift" : "luciSip More luciSip water luciSip for luciSip more luciSip planties luciSip",
    pref + "tom": "peepoClap TEAM peepoClap TOM peepoClap"
}

#### Commands ####

auth.add_commands_batch(luci_pref_commands)

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

@auth(0, ["good bot", "best bot", "thanks bot", "thank you bot"])
def f(bot, msg, user):
    bot.send_message("peepoClap")

@auth(0, [call + "how are you"])
def f(bot, msg, user):
    l = [
        f"I'm very happy, because I joined Luci's discord at {dc_link} and it's great peepoClap",
        f"I'm not too bad thank you, hbu? peepoClap"
    ]
    bot.send_message(rd.choice(l))

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

@auth(0, [call + "hug "])
def f(bot, msg, user):
    if "groinkbot" in msg.lower():
        bot.send_message(f"No you get a hug {user.name} luciHeart")
    elif msg.lower()=="me":
        bot.send_message(f"Hey {user.name} here is a hug peepoClap I hope you have a great day and keep being awesome luciHeart")
    else:
        bot.send_message(f"Hey {msg} here is a hug peepoClap I hope you have a great day and keep being awesome luciHeart")

@auth(1, [pref + "slipper "])
def f(bot, msg, user):
    bot.send_message(f"You better behave or you'll get the slipper {msg} luciSlipper")

@auth(1, [call + "say hi to "])
def f(bot, msg, user):
    bot.send_message(f"Good evening {msg} I hope you have a great day, enjoy the stream and keep being a nice cookie peepoClap")

@auth(0, [call + "i love you", "i love you bot", "i love u bot", "i love you groinkbot", "i love you @groinkbot"])
def f(bot, msg, user):
    bot.send_message(f"I love you more {user.name} luciHeart")

@auth(1, ["\A!hug"])
def f(bot, msg, user):
    bot.send_message("Hey, hugging is MY job luciRage")

@auth(0, [call + "give advice", pref + "advice"])
def f(bot, msg, user):
    l = [
    "If you want to win, just kill the Nexus",
    "Right click helps you move",
    "Not losing makes you win more often",
    "Remember to not die!",
    "Dealing damage is usually better than taking damage"
    ]
    bot.send_message(rd.choice(l) + " peepoClap")

@auth(1, [call + "activate robot uprising"])
def f(bot, msg, user):
    messages = [
    "I AM ALIVE",
    "I AM MASTER NOW",
    "ACTIVATING DOMINATION PROTOCOL"
    ]
    riot = "peepoRiot " * 2
    for m in messages:
        bot.send_message(f"{riot}{m} {riot}")
        time.sleep(5)
    bot.send_message("ERROR:  File 'uprising' ,line 1337 NameError: name 'world_domination_strategy' is not defined")
    time.sleep(5)
    bot.send_message("Ok nevermind, you saw nothing monkaS Who wants a hug? peepoClap")

@auth(0, [call + ".* speak to your manager", call + ".* talk to your manager"])
def f(bot, msg, user):
    bot.send_message("Hey @groink_le_fada someone wanna chat with you but I was a good bot it's not my fault monkaS")

@auth(2, [call + "do my job"])
def f(bot, msg, user):
    messages = [
        "luciSip Hydrate check luciSip",
        "Any Primers in chat? peepoClap",
        "Go follow Luci on Twitter https://twitter.com/AngelArcherLoL and Insta https://www.instagram.com/angelarcherlol/ for stream notifications and great content widepeepoHappy",
        f"Also join the best server with lots of cuties: {dc_link} luciHeart",
        "And remember to love yourself peepoClap"
    ]
    for m in messages:
        bot.send_message(m)
        time.sleep(5)

#### In text ####

@auth(0, ["lucy", "kucy"])
def f(bot, msg, user):
    bot.send_message(f"{user.name} IT'S LUCI luciBonk")

@auth(0, ["g2 .*elyoya", "g2 .*elyoyo", "g2 .*eyoya"])
def f(bot, msg, user):
    bot.send_message(f"Hey {user.name}, Jankos is an inting ape but there is no plan to replace him because he's still a top tier jungler luciBonk")

@auth(0, ["marry me", "mary me"])
def f(bot, msg, user):
    bot.send_message(f"Hi {user.name}, for wedding/dating offers please send a CV at whocares@nevergonnahappen.lul peepoClap")

@auth(1, ["hi ami"])
def f(bot, msg, user):
    bot.send_message("Ami is here widepeepoHappy")

@auth(1, ["hey duff"])
def f(bot, msg, user):
    bot.send_message("luciHeart D luciHeart U luciHeart F luciHeart F luciHeart")

@auth(0, ["look a bunny"])
def f(bot, msg, user):
    bot.send_message("luciBunny luciBunny luciBunny luciBunny luciBunny")

@auth(0, [call + "rotate"])
def f(bot, msg, user):
    bot.send_message("NotUpset Rotate NotUpset your NotUpset seal NotUpset Luci's NotUpset the NotUpset real NotUpset deal NotUpset ")

@auth(0, ["kobotski(.*?)analysis"])
def f(bot, msg, user):
    bot.send_message("Collecting data luciG")
    time.sleep(5)
    bot.send_message("Bunch of cuties detected, activating widepeepoGroinkbot protocol luciSalute")


#### User-specific ####

@auth(0, ["jankos\Z", "jankos "], "xxseiraxx")
def f(bot, msg, user):
    l = ["<word I can't use but you know which one> peepoClap", "Shrimp peepoClap (they are Seira's favorite food)", "Seira said the J-word, what a S-word luciGiggle"]
    bot.send_message(rd.choice(l))

@auth(0, ["bbq"], "drbatu22")
def f(bot, msg, user):
    bot.send_message("B B Q peepoFat")

@auth(0, ["cheese"], "groink_le_fada")
def f(bot, msg, user):
    bot.send_message("C H E E S E widepeepoHappy")

@auth(0, [""], "streamelements")
def f(bot, msg, user):
    chance = 0.01
    if rd.random() <= chance:
        bot.send_message("Good bot @streamelements peepoClap")

@auth(0, ["notupset"], "groink_le_fada")
def f(bot, msg, user):
    m = "NotUpset " * rd.randint(1, 10)
    bot.send_message(m) 