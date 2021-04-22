from ..modular_core import call, pref, BluePrint, rd, time, hello
auth = BluePrint()

from PIL import Image, ImageFont, ImageDraw
from inky.auto import auto
from font_fredoka_one import FredokaOne

class InkyTouchCMD:
    def __init__(self, bot=None):
        self.inky_display = auto(ask_user=True, verbose=True)
        self.resolution = (self.inky_display.WIDTH, self.inky_display.HEIGHT)
        self.img = Image.new("L", self.resolution)
        self.draw = ImageDraw.Draw(self.img)

        self.bot = bot
        self.touchmodule = None
        self.cmds = {}

        self.color = self.inky_display.BLACK

        if bot is not None:
            self.fetch_cmds(bot)
            self.update_display()

    def fetch_cmds(self, bot):
        if "touch" in bot.modules.keys():
            self.touchmodule = bot.modules["touch"]
            self.cmds = self.touchmodule.touch_commands
            self.cmds["E"] = self.cmds["Enter"]
            self.bot = bot
            return True
        return False

    def update_display(self):
        self.img = Image.new("L", self.resolution)
        self.draw = ImageDraw.Draw(self.img)
        touches = ["A", "B", "C", "D", "E"]
        delta_y = int(self.resolution[1] / 5)
        for i in range(5):
            t = touches[i]
            m = self.cmds[t]
            t = t + ": "
            self.draw.text((0, delta_y*i), t, self.color, font=font)

            x = font.getsize(t)[0]
            self.draw.text((x, delta_y*i + 2), m, self.color, font=font_smol)
        self.inky_display.set_image(self.img)
        self.inky_display.show()
        if self.touchmodule is not None:
            self.touchmodule.tp.all_off()

font = ImageFont.truetype(FredokaOne, 22)
font_smol = ImageFont.truetype(FredokaOne, 18)

inky = InkyTouchCMD()

def link(bot):
    inky.fetch_cmds(bot)
    inky.update_display()
    print(f"Inky connected")

def unlink(bot):
    print(f"Inky disconnected")

def reload(bot):
    inky.fetch_cmds(bot)
    inky.update_display()
    print(f"Inky reloaded", inky.cmds)
