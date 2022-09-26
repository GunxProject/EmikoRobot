# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import random

from EmikoRobot.events import register
from EmikoRobot import telethn as tbot, ubot2

from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(pattern="^/asupan(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari Video Asupan...**")
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.inter_messages(
                "@IndomieGantengV3", filter=InputMessagesFilterVideo
            )
        ]
        
        await tbot.send_file(
            event.chat_id,
            file=random.choice(asupannya), reply_to=event.reply_to_msg_id,
            caption=f"**Asupan by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan video asupan.**")


@register(pattern="^/desahcewe(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari VN Desahan Cewe...**")
    try:
        desahannya = [
            desah
            async for desah in ubot2.inter_messages(
                "@IndomieGanteng", filter=InputMessagesFilterVoice
            )
        ]
        
        await tbot.send_file(
            event.chat_id,
            file=random.choice(desahannya), reply_to=event.reply_to_msg_id,
            caption=f"**Desahan by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan vn desahan cowo.**")


@register(pattern="^/desahcowo(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari VN Desahan Cowo...**")
    try:
        desahcowo = [
            desahnya
            async for desahnya in ubot2.inter_messages(
                "@desahancowok3", filter=InputMessagesFilterVoice
            )
	]
        
        await tbot.send_file(
            event.chat_id,
            file=random.choice(desahcowo), reply_to=event.reply_to_msg_id,
            caption=f"**Desahan cowo by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan desahan cowo.**")


@register(pattern="^/ayang(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari Ayang...**")
    try:
        ayangnya = [
            ayang
            async for ayang in ubot2.inter_messages(
                "@IndomieGantengV2", filter=InputMessagesFilterPhotos
            )
        ]
        
        await tbot.send_file(
            event.chat_id,
            file=random.choice(ayangnya), reply_to=event.reply_to_msg_id,
            caption=f"**Ayang by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")

