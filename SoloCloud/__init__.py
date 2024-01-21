from SoloCloud.core.bot import AyushSolo
from SoloCloud.core.dir import dirr
from SoloCloud.core.git import git
from SoloCloud.core.userbot import Userbot
from SoloCloud.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()
# sudo()

app = AyushSolo()
userbot = Userbot()


from .platforms import *

Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
