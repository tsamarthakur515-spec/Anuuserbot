import asyncio
import os
import signal
import sys
import subprocess
from aiohttp import web
from telethon import TelegramClient, events
from telethon.sessions import StringSession
import config
import bot_handlers
import user_handlers
from session import userbot, active_users, client_users, set_ping
from config import bot

# ─────────── Kill Old Instances ───────────
def kill_old_instances():
    try:
        result = subprocess.run(["pgrep", "-f", "main.py"], capture_output=True, text=True)
        for pid in result.stdout.splitlines():
            if pid and int(pid) != os.getpid():
                print(f"🔪 Killing old bot process PID: {pid}")
                os.kill(int(pid), signal.SIGKILL)
    except Exception as e:
        print(f"⚠️ Could not auto-kill old instances: {e}")

kill_old_instances()

PORT = int(os.getenv("PORT", 10000))

# ─────────── Web Server ───────────
async def handle(request):
    return web.Response(text="✅ Bot is alive!")

async def start_web():
    global PORT
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()

    while True:
        try:
            site = web.TCPSite(runner, "0.0.0.0", PORT)
            await site.start()
            print(f"""
---------------------------------
sᴀᴍᴀʀ ᴛʜᴀᴋᴜʀ ᴀʟʟ ᴍᴏᴅᴜʟᴇs ʟᴏᴀᴅᴇᴅ
   ᴀɢʏᴀ ᴛᴜᴍ sᴀʙᴋɪ ɢᴀɴᴅ ᴍᴀʀɴᴇ 
  ᴏᴡɴᴇʀ:- @ll_Sexcy_Samar_ll
---------------------------------
""")

            return runner
        except OSError as e:
            if e.errno == 98:  # Address already in use
                print(f"⚠️ Port {PORT} is busy. Trying next...")
                PORT += 1
            else:
                raise

# ─────────── Userbot Manager ───────────
async def run_userbot(session_str):
    while True:
        if session_str in active_users:
            await asyncio.sleep(5)
            continue
        active_users.add(session_str)
        client = TelegramClient(StringSession(session_str), config.API_ID, config.API_HASH)
        try:
            await client.start()
            user_handlers.register(client)
            me = await client.get_me()
            client_users(me)
            print(f"✅ Userbot {me.first_name} started")
            await client.run_until_disconnected()
        except Exception as e:
            print(f"❌ Userbot error: {e}")
            await asyncio.sleep(5)
        finally:
            if session_str in active_users:
                active_users.remove(session_str)
            await client.disconnect()

async def manage_userbots():
    while True:
        sessions = userbot.get("client", [])
        for session_str in sessions:
            if session_str not in active_users:
                asyncio.create_task(run_userbot(session_str))
        await asyncio.sleep(5)

# ─────────── Main Bot ───────────
async def run_main_bot():
    while True:
        client = TelegramClient("bot_session", config.API_ID, config.API_HASH)
        try:
            await client.start(bot_token=config.BOT_TOKEN)
            set_ping()
            bot_handlers.register(client)
            me = await client.get_me()
            bot["name"] = me.first_name
            bot["username"] = me.username
            bot["user_id"] = me.id
            print(f"🤖 Main bot @{me.username} started")
            await client.run_until_disconnected()
        except Exception as e:
            print(f"❌ Main bot crashed: {e}")
            await asyncio.sleep(5)
        finally:
            await client.disconnect()

# ─────────── Entry Point ───────────
async def main():
    await start_web()
    asyncio.create_task(manage_userbots())
    await run_main_bot()
                  # Start main bot

def handle_exit(signum, frame):
    print("🛑 Shutting down...")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_exit)
    signal.signal(signal.SIGTERM, handle_exit)
    asyncio.run(main())


