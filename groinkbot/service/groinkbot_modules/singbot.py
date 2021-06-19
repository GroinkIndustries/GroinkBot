from ..modular_core import call, pref, BluePrint, rd, time
auth = BluePrint()

def link(bot):
    print(f"SingBot connected")

def unlink(bot):
    print(f"SingBot disconnected")

#### Singing ####

songs = {
    "test" : ["This is a song", "And I sing it"],
    "on my mind" : ["You stay on my mind", "Think about you all the time", "Gotta get to know you well", "If you kiss then I won't tell"],
    "turtle" : ["A turtle lives in water", "A tortoise lives on land","A turtle's not a tortoise it's not hard to understand", "TUUUUURTLE", "YAYAYAYAYA", "TURTLE TURTLE TURTLE"],
    "duck" : ["A duck walked up to a lemonade stand", "And he said to the man, running the stand", "Hey! (Bum bum bum) Got any grapes?", "Then he waddled away, Waddle waddle", "Til the very next day Bum bum bum bum ba-bada-dum"],
    "lec back" : ["I want the LEC back so I can spam in the chat", "I want the LEC back in my life", "Rap Battles, Medi-Vedi, feelin' all right", "I want the LEC back tonight"],
    "submarine": ["We all live in a yellow submarine", "Yellow submarine, yellow submarine", "We all live in a yellow submariiine", "Yellow submariiine, yellow submariiine"],
    "hakuna matata": ["Hakuna Matata! What a wonderful phrase", "Hakuna Matata! Ain't no passing craze", "It means no worries For the rest of your days", "It's our problem-free philosophy", "Hakuna Matata!"],
    "nico":["nico nico nii!", "anata no haato ni nico nico nii", "egao no todokeru yazawa nico nico!", "Nico Nii oboete Rabu nico!"],
    "darude sandstorm":["Duuuuuuuuuuuuuuuuuuuuuuun duDudu ", "Dun dun dun dun dun dun duDudu dun dun dun dun dun dundun dun duDudu ", "dundundun dun dun dun dun duDudu dun dun dundun dundun duDudu", "BOOM duDudu Dundun dundun dundun", "BEEP duDudu Dun dun dun dun dun Dun dun"],
    "saul's song": ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you"],
    "baby shark": ["Baby shark, doo, doo, doo, doo, doo, doo", "Mommy shark, doo, doo, doo, doo, doo, doo", "Daddy shark, doo, doo, doo, doo, doo, doo", "Grandma shark, doo, doo, doo, doo, doo, doo", "Grandpa shark, doo, doo, doo, doo, doo, doo", "Let's go hunt, doo, doo, doo, doo, doo, doo"],
    "tata lex": ["Tata Lex doo, doo, doo, doo, doo, doo", "Best Auntie doo, doo, doo, doo, doo, doo", "Let's go play doo, doo, doo, doo, doo, doo", "Make wine cold doo, doo, doo, doo, doo, doo",  "Luci GIFs doo, doo, doo, doo, doo, doo"],
    "fox": ['Dog goes "woof", Cat goes "meow", Bird goes "tweet" and mouse goes "squeek"', 'Cow goes "moo", Frog goes "croak" and the elephant goes "toot"', 'Ducks say "quack" and fish go "blub" and the seal goes "ow ow ow"',
        "But there's one sound That no one knows", 'What does the fox say? "Ring-ding-ding-ding-dingeringeding!"', 'What the fox say? "Wa-pa-pa-pa-pa-pa-pow!'],
    "dance with me": ["Come on dance with me, we're the LEC", "Come on dance with me, let yourself be free", "Come on dance with me, we're the LEC", "Come on dance with me, do that PepeD"],
    "rekkles":["BACKSTABBED By the one who I loved most", "BETRAYED How am I supposed to cope", "I should be glad that we’re apart When you’re so Rekkles with my heart",
        "REVENGE For the wound that you can't see", "REBIRTH From the ashes where you left me", "And when your tear is fully stacked  I know that you’ll come crawling back"],
    "bet on it":["I'm not gonna stop, that's who I am", "I'll give it all I got, that is my plan", "When I find what I lost You know you can", "Bet on it, bet on it, Bet on it, bet on it"],
    "ankleville":["A duck walked up to the Ankleville stand", "And he said to the woman, running the stand: Hey! (Bum bum bum) Got any peeps?", "No we just sell cuties, but they cute and they sweet and they all make my day. Can I get you one?", "The duck said: I'll pass! Then he waddled away"],
    "crown":["We fight for those you left behind", "We live for those who were denied ", "We know your fate is set in stone", "We've come to take the throne"],
    "lec rap": ["Back to back to back", "You know these titles start to stack", "Just like all your failed splits", "Start to think that this is it"],
    "butter": ["Side step, right, left to my beat", "High like the moon, rock with me, baby", "Know that I got that heat", "Let me show you 'cause talk is cheap", "Side step, right, left to my beat"]
}

@auth(1, [call + "sing hb to "])
def f(bot, msg, user):
    l = ["Happy birthday to you", "Happy birthday to yoouu", f"Happy birthday dear {msg}", "Happy birthday to you"]
    sing_song(bot, l)

def sing_song(bot, lyrics):
    emotes = ["blobDance ", "pepeD "] # catJAM
    emote = rd.choice(emotes) * 2
    for m in lyrics:
        bot.send_message(f"{emote}{m} {emote}")
        time.sleep(5)

def sing_song_name(bot, name):
    messages = songs[name]
    sing_song(bot, messages)

@auth(0, [pref + "botsongs"])
def f(bot, msg, user):
    s = "Available songs are: "
    s += ", ".join(list(songs.keys()))
    s+= " blobDance"
    bot.send_message(s)

@auth(1, [call + "sing for me", pref + "sing"])
def f(bot, msg, user):
    name = rd.choice(list(songs.keys()))
    sing_song_name(bot, name)

@auth(1, [call + "sing +"])
def f(bot, msg, user):
    if msg in songs.keys():
        sing_song_name(bot, msg)
    else:
        bot.send_message(f"Sorry I don't know the '{msg}' song")
