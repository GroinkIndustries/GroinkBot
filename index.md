# GroinkBot 

Groinkbot is a multi-plateform framework for chatbots, based on a `service` - `interface` structure.

## Service
A service is the brain of a bot, what allows it to process commands, and answer or do other actions. 

The main service here is [ModularBot](https://github.com/GroinkIndustries/GroinkBot/blob/master/groinkbot/service/modular.py), which allows for the modular development of bots and dynamic code loading. it can load [standard modules](https://github.com/GroinkIndustries/GroinkBot/tree/master/groinkbot/service/groinkbot_modules) from their file names (`singbot` for load the file `singbot.py`), and custom files if defined correctly.

## Interface

An interface connects to a source (eg a Twitch chat, Discord channel, or an input in command line) and processes the messages to be sent to a service with a standard format.


# Install
To install the bot, run:
```bash
git clone https://github.com/GroinkIndustries/GroinkBot.git
cd GroinkBot
pip install . 
```

If libraries are missing, run:
```
pip install discord.py irc pandas
```

# Demo

## Create a bot
```python
from groinkbot.service.modular import ModularBot
gb = ModularBot()
gb.add_standard_modules(["basic", "singbot"]) # Add standard modules
```

## Add an interface
### Command line
```python
from groinkbot.interface.cli_interface import CLIInterface
bot = CLIInterface(gb)
bot.start()
```

### Twitch
Register an app at https://dev.twitch.tv/docs/authentication#registration to get a client_id and a security token.

```python
from groinkbot.interface.twitch import Twitch

roles = {
        "groink_le_fada":3,
        "angelarcherlol":2,
        "duffmanlol":1
}

twitch_auth = {
    "client_id":"XXXXXXXXXXXXXXXXXXXXXXX",
    "token":"XXXXXXXXXXXXXXXXXXXXXXX",
    "username":"GroinkBot" # Bot username
  }

channel = "#groinkbot"

bot = Twitch(twitch_auth, roles, gb, channel=channel)
bot.start()
```

### Discord
```python
from groinkbot.interface.discord_interface import Discord

roles = {
        "groink_le_fada":3,
        "angelarcherlol":2,
        "duffmanlol":1
}

dc_auth = {
  "token":"XXXXXXXXXXXXXXXXXXXXX.XXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXX",
  "guild":"<Server Name>",
  "channel":"<channel>"
}

bot = Discord(dc_auth, roles, gb, guild="Notes")
bot.start()
```

## Adding a custom module
### Creating a module
Custom functions can be added to a ModularBot if they follow this format:
```python
# in new_module.py
from groinkbot.service.modular_core import call, pref, BluePrint, rd, time

def link(bot):
    print(f"Module connected")

def unlink(bot):
    print(f"Module disconnected")

auth = BluePrint()

@auth(2, [call + "test_module"])
def f(bot, msg, user):
    bot.send_message("This is the module")
    
```
The `Blueprint` object registers all functions passed through the generator, to add them when it is imported by the ModularBot.

`link` and `unlink` are used when loading and unloading the module, and are necessary for the module to be accepted.

## Loading the module
The module can be loaded with 
```python
gb.import_module("new_module", "test")
```
With `new_module` the path to the python file, and `test` its name in the bot.

## Adding commands
Commands are added to the "`auth`" `Blueprint` object when the file is imported, then added to the bot. 

```python
@auth(2, [call + "test_module"])
```
The first argument, `2`, is the auth level required to run this command.  
The second argument is the list of regular expressions that can trigger the command, and `call` is the pattern of checking if the message starts with "hey bot".

If there is a 3rd argument, only the person with that name can trigger that command:
```python
@auth(0, ["notupset"], "groink_le_fada")
```

3 arguments are passed to each function defining the actions to do once the command is triggered:
```python
@auth(2, [call + "test"])
def f(bot, msg, user):
    bot.send_message("This is the module")
```
`bot` is the bot, which allows to send messages back.  
`msg` is the rest of the message without the command triggering it, which allows to make commands with parameters  
`user` is an named tuple with the raw name, the name in lowercase and the auth level ("righs") of the person who sent the message:

```python
User = namedtuple('User', 'name lowername rights')
```

## Auth management

Commands can be limited to some categories of people based on they authorization level. Each level is defined by a positive integer, `0` being the default value for anyone not specifically registered.

Assigning a level to someone is based on their id from the interface, in a dictionary when setting up the bot: 
```python
roles = {
        "groink_le_fada":3,
        "angelarcherlol":2,
        "duffmanlol":1
}
```
Here, level 3 is the bot owner, level 2 are mods, and level 1 are priviledged users. The auth level is compare to the required auth when triggering a command, and the command is executed only if the auth level of the person is equal or higher to the required auth level.
