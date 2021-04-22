import pandas as pd
import requests

from ..modular_core import call, pref, BluePrint, rd, time
auth = BluePrint()


def link(bot):
    print(f"Pets shelter connected")

def unlink(bot):
    print(f"Pets shelter disconnected")

pet_dfs = pd.read_csv("service/groinkbot_modules/pets_texts.csv", index_col=0)

@auth(0, [pref + "doggo"])
def f(bot, msg, user):
    t = pet_dfs[pet_dfs["type"]=="dogs"].sample()["text"].item()
    bot.send_message(t)

@auth(0, [pref + "catto"])
def f(bot, msg, user):
    t = pet_dfs[pet_dfs["type"]=="cats"].sample()["text"].item()
    bot.send_message(t)

@auth(0, [pref + "mouso"])
def f(bot, msg, user):
    print("Mouse")
    t = "Gerald is a very pretty little mouse that has come to us through no fault of his own. Find more about him at http://lucita.hopto.org/small_animals/gerald/9395/ peepoClap"
    bot.send_message(t)

@auth(0, [pref + "pets"])
def f(bot, msg, user):
    # t = pet_dfs.sample()["text"].item()
    t = "You can find out about the doggos and cattos at http://lucita.hopto.org, or with !doggo, !catto and !mouso peepoClap"
    bot.send_message(t)

@auth(0, [pref + "total"])
def f(bot, msg, user):
    url = "https://graphql.justgiving.com/?variables=%7B%22type%22%3A%22FUNDRAISING%22%2C%22slug%22%3A%22angelarcher%22%2C%22preview%22%3Afalse%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22f69b65ef1006b15c6afd8ceeb828885f998de917006e85d330a0c7a9c775c173%22%7D%7D"
    d = requests.get(url).json()["data"]
    tot = round(d["page"]["donationSummary"]["totalAmount"]["value"]/100)
    message = f"{tot}£ have already been raised peepoClap You can donate at https://www.justgiving.com/fundraising/angelarcher luciHeart"
    bot.send_message(message)
