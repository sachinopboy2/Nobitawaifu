class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1786683163"
    sudo_users = "7990474206", "7282752816"
    GROUP_ID = -1002201996549
    TOKEN = "7647477376:AAEsHX0rQf1NAT6BdlrreCQ85vLrorkQcyY"
    mongo_url = "mongodb+srv://kumarN:kumarN@kumarn.vxdui.mongodb.net/?retryWrites=true&w=majority&appName=kumarN"
    PHOTO_URL = ["https://telegra.ph/file/ed23556d07d33db18402d.jpg", "https://telegra.ph//file/e64337bbc6cdac7e6b178.jpg"]
    SUPPORT_CHAT = "NYCREATION_CHATZONE"
    UPDATE_CHAT = "NOXXNETWORK"
    BOT_USERNAME = "AmritaxBot"
    CHARA_CHANNEL_ID = "-1002204134287"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
