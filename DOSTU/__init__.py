from DOSTU.core.bot import DOSTU
from DOSTU.core.dir import dirr
from DOSTU.core.git import git
from DOSTU.core.userbot import Userbot
from DOSTU.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = DOSTU()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
