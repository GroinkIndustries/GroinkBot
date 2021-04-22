from ..modular_core import call, pref, BluePrint, rd, time, hello
auth = BluePrint()

def link(bot):
    print(f"GIFs connected")

def unlink(bot):
    print(f"GIFs disconnected")


GIFS = {
    "luciD":    "https://media.discordapp.net/attachments/737439845546196992/802875744245252106/Luci_dance_better.gif", 
    "what":     "https://media.discordapp.net/attachments/752906198290006126/756231605336539216/what.gif",
    "bunny":    "https://media.discordapp.net/attachments/755527470945402921/767089451779620884/ezgif.com-crop5-2.gif",
    "vibe":     "https://media.discordapp.net/attachments/737439845546196992/802876088035704832/Dance_Luci2.gif", 
    "clap":     "https://media.discordapp.net/attachments/725113155373629470/774025513756000256/Luci_clap.gif",
    "boogie":   "https://media.discordapp.net/attachments/737439845546196992/802875717473009664/boogie_Luci.gif"
}


@auth(0, [pref + "gif "])
def f(bot, msg, user):
    print(f">{msg}<")
    if msg in GIFS.keys():
        g = GIFS[msg]
        bot.send_message(g)
    else:
        bot.send_message(f"{msg} is not a known GIF")

@auth(0, [pref + "gifs"])
def f(bot, msg, user):
    l = list(GIFS.keys())
    bot.send_message("Here is my GIF library: " + ", ".join(l))