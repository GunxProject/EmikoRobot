# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import random

from EmikoRobot.events import register

from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(pattern="^/asupan(.*)")
async def _(event):
    memek = await event.reply(event, "**🔍 Mencari Video Asupan...**")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@IndomieGantengV3", filter=InputMessagesFilterVideo
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya), reply_to=event.reply_to_msg_id,
            caption=f"**Asupan by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan video asupan.**")


@register(pattern="^/desahcewe(.*)")
async def _(event):
    memek = await event.reply(event, "**🔍 Mencari VN Desahan Cewe...**")
    try:
        desahannya = [
            desah
            async for desah in event.client.iter_messages(
                "@IndomieGanteng", filter=InputMessagesFilterVoice
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahannya), reply_to=event.reply_to_msg_id,
            caption=f"**Desahan by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan vn desahan cowo.**")


@register(pattern="^/desahcowo(.*)")
async def _(event):
    memek = await event.reply(event, "**🔍 Mencari VN Desahan Cowo...**")
    try:
        desahcowo = [
            desahnya
            async for desahnya in event.client.iter_messages(
                "@desahancowok3", filter=InputMessagesFilterVoice
            )
	]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahcowo), reply_to=event.reply_to_msg_id,
            caption=f"**Desahan cowo by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan desahan cowo.**")


@register(pattern="^/ayang(.*)")
async def _(event):
    memek = await event.reply(event, "**🔍 Mencari Ayang...**")
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@IndomieGantengV2", filter=InputMessagesFilterPhotos
            )
        ]
        aku = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya), reply_to=event.reply_to_msg_id,
            caption=f"**Ayang by** [{aku.first_name}](tg://user?id={aku.id})")

        await memek.delete()
    except Exception:
        await memek.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")

