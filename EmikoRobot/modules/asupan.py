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
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Asupan Bergizinya Deck**",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan video asupan. Jangan nakal kamu.**")


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
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Desah Menyegarkannya Om**",
            file=pantek
            )
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
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Desah Menyegarkannya Tante**",
            file=pantek
            )
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
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Ayang Untukmu. Jaga Baik-Baik. Jangan Cari Lagi.",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENK.**")
