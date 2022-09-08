import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "12962251"))
    API_HASH = os.environ.get("API_HASH", "b51499523800add51e4530c6f552dbc8")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "IQmusicxbot")
    SUPPORT = os.environ.get("SUPPORT", "IQerenh")
    CHANNEL = os.environ.get("CHANNEL", "xv7amo")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/43380f5c2ed913e8add36.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/43380f5c2ed913e8add36.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # required
