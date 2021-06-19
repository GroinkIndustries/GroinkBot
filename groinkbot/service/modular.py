from .bot import Bot
import importlib
import re
import os

def find_command(bot, message, commands, user):
    m_low = message.lower()
    for c, m in commands.items():
        if re.search(c, m_low) is not None:
            message = re.sub(c, "", message, flags=re.IGNORECASE)
            if type(m) == str:
                bot.send_message(m)
            else:
                m(bot, message, user)
            return

class ModularBot(Bot):

    def __init__(self):
        Bot.__init__(self)
        self.modules = {}

        # Start with !
        self.pref_commands = {}
        # Starts with "hey bot"
        self.call_commands = {}
        # No special format
        self.text_commands = {}

        self.cmds = importlib.import_module("groinkbot.service.modular_core")
        self.modules["cmds"] = self.cmds

    def __repr__(self):
        r = f"<GroinkBot | {self.interface.__repr__()} |"
        for m in self.modules.keys():
            r += " " + m
        return r + ">"

    def import_blueprint(self, blueprint):
        self.pref_commands = {**self.pref_commands, **blueprint.pref_commands}
        self.call_commands = {**self.call_commands, **blueprint.call_commands}
        self.text_commands = {**self.text_commands, **blueprint.text_commands}

    def import_module(self, module_path, module_name, **kwargs):
        mod = importlib.import_module(module_path)

        for v in mod.__dict__.values():
            if type(v)==self.cmds.BluePrint:
                self.import_blueprint(v)
        
        self.modules[module_name] = mod
        mod.link(self, **kwargs)
        return mod

    def reload(self):
        # Start with !
        self.pref_commands = {}
        # Starts with "hey bot"
        self.call_commands = {}
        # No special format
        self.text_commands = {}

        self.cmds = importlib.import_module("groinkbot.service.modular_core")
        self.modules["cmds"] = self.cmds
        
        for name, module in self.modules.items():
            try:
                module.reload(self)
            except:
                module.unlink(self)
                mod=importlib.reload(module)
                for v in mod.__dict__.values():
                    if type(v)==self.cmds.BluePrint:
                        self.import_blueprint(v)    
                mod.link(self)
                self.modules[name]=mod
        self.cmds = self.modules["cmds"]

    def on_welcome(self):
        self.send_message = self.interface.send_message
        self.interface.send_message(self.cmds.join())

    def get_message(self, message, user):
        # Remove multi-spaces and @
        message = re.sub(" +", " ", message).replace("@", "")
        # Remove spaces at the end
        message = re.sub(" +\Z", "", message)
        m_low = message.lower()
        if re.search(self.cmds.pref, m_low) is not None:
            find_command(self, message, self.pref_commands, user)
        elif re.search(self.cmds.call, m_low) is not None:
            find_command(self, message, self.call_commands, user)
        else:
            find_command(self, message, self.text_commands, user)
    
    def add_standard_modules(self, module_list):
        if type(module_list) == str:
            module_list = [module_list]
        for m in module_list:
            self.import_module(f"groinkbot.service.groinkbot_modules.{m}", m)

    def remove_modules(self, module_list):
        if type(module_list) == str:
            module_list = [module_list]
        for m in module_list:
            self.modules.pop(m)
        self.reload()
