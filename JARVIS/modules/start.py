from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
    ],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/ABOUT_LEGEND_OWNER"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/ABOUT_LEGEND_OWNER")
    ],
    [
        Button.url("• ʀᴇᴘᴏ •", "chal nikl madhr chod")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        ANNIE = await event.client.get_me()
        bot_name = ANNIE.first_name
        bot_id = ANNIE.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [—͟͞͞★⎯꯭̽𓆩〭〬༎꯭𝆺꯭꯭𝅥🥵❘⃟꯭𝄄.꯭꯭🇱꯭꯭ᴇ꯭ɢ꯭֟፝ᴇ꯭ɴ꯭ᴅ 𝆺꯭꯭𝅥༎𓆪꯭꯭⎯꯭⎯꯭̽💗  ★](https://t.me/l_CDX_L3G3ND_l)**\n\n"
        TEXT += f"» **ᴢᴇxx V2 :** `M 1.8.31`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
              event.chat_id,
                    "https://telegra.ph/file/9db8e5d62d2a3b77a14ba.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
