import asyncio
from telethon import errors

async def aru_handle(client, event):
    # try to delete the command message (force)
    try:
        await client.delete_messages(event.chat_id, [event.message.id])
    except Exception as e:
        print(f"⚠️ Could not delete .sm command: {e}")

    messages = [
        "ʙᴀʙᴜ ᴅʜᴇʀ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ ʏᴀʜɪ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ ʏᴀʜɪ ᴘᴇ",
        "ʙᴀʙᴜ ᴅʜᴇʀ ᴍᴀᴛ ʙᴏʟɴᴀ ɴᴀʜɪ ᴛᴏ ʏᴀʜɪ ᴘᴇ ᴘᴀʟᴇ ᴅᴇɴɢᴇ 💀",
        (
            "ғᴜᴍᴋᴇᴅ ʙʏ\n"
            ".                       /¯ )\n"
            "                      /¯  /\n"
            "                    /    /\n"
            "              /´¯/'   '/´¯¯•¸\n"
            "          /'/   /    /       /¨¯\\ \n"
            "        ('(   (   (   (  ¯~/'  ')\n"
            "         \\                        /\n"
            "          \\                _.•´\n"
            "            \\              (\n"
            "              \\--------------\n"
            "               ))))))))))))\n"
            "ғᴜᴍᴋᴇᴅ ʙʏ :- <a href='http://t.me/MANIAC_USR_BOT'>[ ˹sᴜʀᴜᴄʜɪ × ɴᴇᴛᴡᴏʀᴋ˼ ]</a>\n"
            "𝗢𝗪𝗡𝗘𝗥 @ll_Sexcy_Samar_ll\n"
        )
    ]

    if not messages:
        return

    # send the first message (so we have a clean Message object to edit)
    try:
        msg_obj = await client.send_message(event.chat_id, messages[0])
    except Exception as e:
        print(f"❌ Failed to send initial message: {e}")
        return

    base_delay = 0.1  # safe default (0.7-1.0); increase if edits still stop

    # loop edits starting from the second element (0 already sent)
    for i in range(1, len(messages)):
        text = messages[i]
        try:
            await msg_obj.edit(text)
            print(f"✏️ Edited step {i}: {text[:30]}...")
        except errors.MessageNotModifiedError:
            # if the text is same as current, just continue
            print(f"ℹ️ Step {i} text not modified; skipping.")
        except errors.MessageIdInvalidError:
            # can't edit (maybe message lost) -> fallback to sending new message and continue
            print(f"⚠️ MessageIdInvalid at step {i}, sending new message as fallback.")
            try:
                msg_obj = await client.send_message(event.chat_id, text)
            except Exception as e:
                print(f"❌ Fallback send failed at step {i}: {e}")
                return
        except Exception as e:
            # other errors -> try to recover by sending a fresh message
            print(f"⚠️ Edit failed at step {i}: {e}. Attempting to send new message.")
            try:
                msg_obj = await client.send_message(event.chat_id, text)
            except Exception as ex:
                print(f"❌ Fallback send failed at step {i}: {ex}")
                return

        # longer pause before the final big ASCII art for readability
        if i == len(messages) - 1:
            await asyncio.sleep(0.1)
        else:
            await asyncio.sleep(base_delay)
