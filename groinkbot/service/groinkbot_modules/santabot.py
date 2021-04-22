from ..modular_core import call, pref, BluePrint, rd, time
auth = BluePrint()

def link(bot):
    print(f"SantaBot connected")

def unlink(bot):
    print(f"SantaBot disconnected")

#### SantaBot ####

def santa_message(bot, message, default_color="springgreen"):
    bot.send_message("/color goldenrod")
    bot.send_message(f"/me pepeSanta SoSnowy HoHoHo, {message} pepeSanta SoSnowy ")
    bot.send_message(f"/color {default_color}")

@auth(1, [call + "i have cookies and milk"])
def f(bot, msg, user):
    bot.send_message("Great, I will call my friend SantaBot peepoClap")
    time.sleep(5)
    santa_message(bot, "I am SantaBot")
    time.sleep(2)
    santa_message(bot, "with me good peepos get Christmas gifts peepoClap")

@auth(0, [pref+"santa"])
def f(bot, msg, user):
    bot.send_message('Ask "Hey bot have I been a good peepo" if you want a present peepoClap')

adj = [
"flying", "magical", "glowing", "friendly", "sparkling", "kind", "noisy", "classy", "psychedelic"
]
names = [
"potato", "teddy bear", "jar of beans", "chocolate bar", "Banana", "Headphone",
"sharpie", "mirror", "helmet", "rubber band", "mop",
"bottle", "cup", "dress", "apple", "clock",
"flower", "bag"
]

gifts = {
"groink_le_fada": "You're so great, your gift is me luciHeart",
"groink": "Groink is my favorite peepo luciHeart",
"luci": "You're the best peepo Luci so you get the best present luciHeart And the best present is me peepoClap",
"angelarcherlol": "You're the best peepo Luci so you get the best present luciHeart And the best present is me peepoClap",
"hexi": "There is no present for Hexi, because no present could bring them as much happiness as being cuties together luciHeart",
"duffmanlol" : "You were a really nice peepo Duffie luciHeart SantaLuci will bring you more stars in 2021 peepoClap",
"duff": "You were a really nice peepo Duffie luciHeart SantaLuci will bring you more stars in 2021 peepoClap",
"lexeda": "You're a really nice peepo even though you put ice in wine, SantaBot shall give you more wine to drown the ice peepoClap",
"cyberfox21": "Nuno widepeepoHappy You get all the love in the world luciHeart",
"drbatu22": "You've been a good BBQ peepo peepoFat You get more BBQ peepoClap peepoClap",
"lenny" : "You're a really good boy, here is a nice bone PettheRoxy",
"groinkbot": "GroinkBot was a good bot peepoClap But the best gift for him is being here with you all luciHeart"
}

def random_item(lowername):
    if lowername in gifts.keys():
        return gifts[lowername]
    l1 = ["You were a great peepo", "You've been a great peepo", "What a great peepo"]
    l2 = ["Your present is", "You shall get", "Under your tree there shall be"]
    m = f"{rd.choice(l1)} {lowername} peepoClap "
    m += f"{rd.choice(l2)} a {rd.choice(adj)} {rd.choice(names)}!"
    return m


@auth(0, [call+".* good peepo"])
def f(bot, msg, user):
    m = random_item(user.lowername)
    santa_message(bot, m)


@auth(1, [call + "call santa for +"])
def f(bot, msg, user):
    m = random_item(msg.lower())
    santa_message(bot, m)

@auth(0, [call + "bonk "])
def f(bot, msg, user):
    m = f"luciBonk BAD {msg.upper()}! You're getting coal for Christmas luciRage"
    santa_message(bot, m)
