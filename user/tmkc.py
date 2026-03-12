import asyncio
from telethon import errors

async def tmkc_handle(client, event):
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
            "ғᴜᴍᴋᴇᴅ ʙʏ :- <a href='https://t.me/suruchisupport'>[ ˹sᴜʀᴜᴄʜɪ × ɴᴇᴛᴡᴏʀᴋ˼ ]</a>\n"
            "ᴏᴡɴᴇʀ :-  <a href='https://t.me/ll_Sexcy_Samar_ll'> [ ᴀs sᴀᴍᴀʀ ]</a>\n"
        )
    ]

    if not messages:
        return

    # send the first message
    try:
        msg_obj = await client.send_message(
            event.chat_id,
            messages[0],
            parse_mode="html"
        )
    except Exception as e:
        print(f"❌ Failed to send initial message: {e}")
        return

    base_delay = 0.1

    # loop edits
    for i in range(1, len(messages)):
        text = messages[i]

        try:
            await msg_obj.edit(
                text,
                parse_mode="html"
            )
            print(f"✏️ Edited step {i}: {text[:30]}...")

        except errors.MessageNotModifiedError:
            print(f"ℹ️ Step {i} text not modified; skipping.")

        except errors.MessageIdInvalidError:
            print(f"⚠️ MessageIdInvalid at step {i}, sending new message.")
            try:
                msg_obj = await client.send_message(
                    event.chat_id,
                    text,
                    parse_mode="html"
                )
            except Exception as e:
                print(f"❌ Fallback send failed at step {i}: {e}")
                return

        except Exception as e:
            print(f"⚠️ Edit failed at step {i}: {e}")
            try:
                msg_obj = await client.send_message(
                    event.chat_id,
                    text,
                    parse_mode="html"
                )
            except Exception as ex:
                print(f"❌ Fallback send failed at step {i}: {ex}")
                return

        if i == len(messages) - 1:
            await asyncio.sleep(0.1)
        else:
            await asyncio.sleep(base_delay)
