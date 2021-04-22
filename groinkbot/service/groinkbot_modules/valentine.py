from ..modular_core import call, pref, BluePrint, rd, time
import hashlib
auth = BluePrint()

def link(bot):
    print(f"Valentine connected")

def unlink(bot):
    print(f"Valentine disconnected")

HEX_LEN = 5
MAX_HEX = int("f"*HEX_LEN*2, 16)

def hash_to_dec(name):
    shake = hashlib.shake_128()
    shake.update(name.encode('utf-8'))
    return int(shake.hexdigest(HEX_LEN), 16)

def get_love(p1, p2):
    h1, h2 = hash_to_dec(p1), hash_to_dec(p2)
    l = (h1+h2)/(2*MAX_HEX)
    return int(100*l)

DUOS={
    "lenny zanelg spacekrieger | maty cosmicsailor": "Mannert has a certified 100% love or whatever luciSalute",
    #"luci angelarcherlol | rekky rekkles ":'Rekki HYPERS I mean who? never heard of rekki wdym monkaS',
    "groink | groinkbot": "Master has made GroinkBot a free elve widepeepoHappy",
    "groinkbot | luci angelarcherlol": "I love everyone equally, but Luci is a bit more equal than the others luciShy luciHeart",
    "seira xxseiraxx | jankos": "Seira is just a shrimp peepoClap",
    "duff duffy duffie duffman duffmanlol | miky mikyx": "Duffyx is obviously a 100% peepoClap",
    "eugi euugi eugynnn | bauti drbatu22": "The BBQ couple has hearts bigger than their stomachs, definitely 100% luciHeart",
    "tsm | groups": "TSM has a 0-6% love with Worlds Groups luciGiggle",
    "grabbz | draft drafting drafts": "Grabbz's drafs KEKW",
    "seira xxseiraxx | elyoyo hirit": "Science says it's a 100% luciG",
    "groink | cheese": "C H E E S E peepoFat",
    "bauti drbatu22 | bbq" : "B B Q peepoFat",
    "luci angelarcherlol | chat" : "Of course luci loves her chat luciHeart",
    "lex lexa lexeda |seira xxseiraxx":"Lexeira is a real GIFt widepeepoHappy",
    "ami heilith | devi": "Demi have a 100% accuracy at being cuties luciAnkle",
    "turtle turtles | tortoise tortoises":  "blobDance blobDanceA turtle's not a tortoise it's not hard to understand blobDance blobDance",
    "duck | grape grapes":"blobDance waddle waddle blobDance",
    "duff | cutie": "Duff has a 100% chance of finding a cutie, because he is a cutie peepoClap",
    "hennie jo johanna | work study working studying": 100,
    "groink groink_le_fada | cyberfox21 nuno":200,
    "bauti drbatu22 | cyberfox21 nuno":199,
    "luci angelarcherlol | ankleville": 100,
    "luci angelarcherlol | groink groink_le_fada": 99,
    "g2 | internet": "There was packet loss, I couldn't compute the love % between G2 and internet luciG"
}

def in_couple(p1, p2, couple):
    l = couple.split("|")
    l0 = l[0].split(" ")
    l1 = l[1].split(" ")
    if p1 in l0 and p2 in l1:
        return True
    if p2 in l0 and p1 in l1:
        return True
    return False

@auth(0, [pref + "love "])
def f(bot, msg, user):
    l = msg.lower().split(" ")
    if len(l) > 1:
        p1, p2 = l[0], l[1]
        if p1 == "me":
            p1 = user.lowername
        if p2 == "me":
            p2 = user.lowername
    else:
        p1 = user.lowername
        p2 = l[0]
        if p2 == "me":
            p2 = user.lowername
    
    if p1 == p2:
        bot.send_message(f"Hey {p1}, data says you should love yourself luciG because you're 100% awesome peepoClap")
        return
        
    
    for k, v in DUOS.items():
        if in_couple(p1, p2, k):
            if type(v) == str:
                bot.send_message(v)
            else:
                bot.send_message(f"There is {v}% love chance between {p1} and {p2} peepoClap")
            return 
    
    if "groinkbot" in [p1, p2]:
        bot.send_message(f"There is 100% love chance between {p1} and {p2} because I love everybody widepeepoHappy")
        return
    
    love = get_love(p1, p2)
    bot.send_message(f"There is {love}% love chance between {p1} and {p2} peepoClap")
    
    
VAL = [
    "Hey {d}, will you be {s}'s valentine? luciShy",
    "Hey {d} you're kinda cute, wanna be {s}'s valentine? luciShy",
    "Hello {d}, I think {s} wants you to be their valentine luciShy",
    "{d} is pretty, {s} is kinda cute, together they'd be pretty cute peepoClap",
    "luciLurk psssst {d}, I think {s} kinda likes you luciHeart",
    "Roses are red, violets are blue, hey {d} {s} kinda likes you blobDance"
]
    
@auth(0, [pref + "valentine "])
def f(bot, msg, user):
    l = msg.split(" ")[0]
    m = rd.choice(VAL).format(s=user.name, d=msg)
    bot.send_message(m)
    
    
# @auth(0, [pref + "valentinebot", pref + "valentine"])
# def f(bot, msg, user):
#     m = "Happy Valentine's day peepoClap "
#     m += 'Send "!valentine {user}" to ask someone luciShy '
#     m += 'Send "!love {user}" to know your chances, or "!love {u1} {u2}" to know the chance of love between 2 people blobDance'
#     bot.send_message(m)
    
    
@auth(0, [pref + "disclaimer"])
def f(bot, msg, user):
    m = "Disclaimer: I was coded by a bored dude, none of what I say is to be taken too seriously peepoClap"
    bot.send_message(m)
    