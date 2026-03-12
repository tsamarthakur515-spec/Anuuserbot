import asyncio

async def help_handle(client, event):
    # Delete the .help command message
    try:
        await event.delete()
    except:
        pass

    # Small animation message
    x = await event.respond("**ᴄᴏᴍɪɴɢ ʙᴀʙʏ....**")
    await asyncio.sleep(0.2)

    # Help Menu
    help_text = """```
🤖 𝐒𝐔𝐑𝐔𝐂𝐇𝐈 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨

𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦
> `.afk`
> `.ban`
> `.ba`
> `.brain`
> `.info`
> `.clone`
> `.dono`
> `.help`
> `.love`
> `.lover`
> `.mute`
> `.nah`
> `.ping`
> `.raid`
> `.marco`
> `.spam`
> `.type`
> `.wtf`

𝗦𝗨𝗣𝗣𝗢𝗥𝗧
𝗖𝗛𝗔𝗡𝗡𝗘𝗟: @suruchisupport
𝗢𝗪𝗡𝗘𝗥: @ll_Sexcy_Samar_ll
```"""

    await x.edit(help_text)
