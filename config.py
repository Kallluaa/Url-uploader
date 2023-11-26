
import os
import dotenv
#import SmartEncoder.Database.db.myDB as db


dotenv.load_dotenv()

class Config(object):
  API_ID = int(os.environ.get("API_ID", 12345))
  API_HASH = os.environ.get("API_HASH")
  BOT_TOKEN = os.environ.get("BOT_TOKEN")
  AUTH_USERS = os.environ.get("AUTH_USERS")
  GOD = os.environ.get("GOD")
  REDIS_HOST = os.environ.get("REDIS_HOST")
 # REDIS_PORT = int(os.environ.get("REDIS_PORT", 12345))
  REDIS_PASS = os.environ.get("REDIS_PASS")
  DOWN_PATH = "./downloads"
  MAX_VIDEOS = int(os.environ.get("MAX_VIDEOS", 15))
  CAPTION = "Video Merged by @{}\n\nMade by @Hkbotzowner"
  PROGRESS = """<b>\n
𝙋𝙧𝙤𝙘𝙚𝙨𝙨𝙞𝙣𝙜... 
🗃️ sɪᴢᴇ : {1} | {2}
⏳ Dᴏɴᴇ : {0}%
🚀 Sᴩᴇᴇᴅ: {3}/s
⏰️ Eᴛᴀ: {4} </b>"""

Config.AUTH_USERS = [1975696269, 1112773045]
#Config.API_ID = 14604313
#Config.API_HASH = "a8ee65e5057b3f05cf9f28b71667203a"
#Config.BOT_TOKEN = "6150084524:AAHutAX3WQjZxQVOxI4vCdlR4tzyRIotMt8"
#Config.REDIS_HOST = "redis-10344.c275.us-east-1-4.ec2.cloud.redislabs.com"
#Config.REDIS_PASS = "2bdmUMBhHt1q7dalbm3MnKbOmWFMsgaP"
#REDIS_PORT = "10344"
Config.REDIS_HOST = "redis-13175.c275.us-east-1-4.ec2.cloud.redislabs.com"
Config.REDIS_PASS = "CUhvPk53v8WxFl1NgU38RFvaMsQ6Yr1z"
REDIS_PORT = "13175"
