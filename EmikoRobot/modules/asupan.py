# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import random

from EmikoRobot.events import register
from EmikoRobot import telethn as tbot, ubot2

from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice
from telethon.tl.types import InputMessagesFilterPhotos


@register(pattern="^/asupann(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari Video Asupan...**")
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
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


@register(pattern="^/desahcewee(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari VN Desahan Cewe...**")
    try:
        desahannya = [
            desah
            async for desah in ubot2.iter_messages(
            "@IndomieGanteng", filter=InputMessagesFilterVoice
            )
        ]
        kontols = random.choice(desahannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Desah Menyegarkannya Om**",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan vn desahan cowo.**")


@register(pattern="^/halletku(.*)")
async def _(event):
    memek = await event.reply("**🔍 Paima da.. Mangalului haletmu jo au tu lapo...**")
    try:
        desahcowo = [
            desahnya
            async for desahnya in ubot2.iter_messages(
            "@xzgshhs0hsjebbe0883bhd", filter=InputMessagesFilterPhotos
            )
	]
        kontols = random.choice(desahcowo)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Halletmu. Jaga Baik - Baik. Jangan Lepas.**",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan halletmu. Mungkin belum lahir.**")


@register(pattern="^/hasianku(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari Ayang...**")
    try:
        ayangnya = [
            ayang
            async for ayang in ubot2.iter_messages(
            "@o0o0llxxz", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(ayangnya)
        pantek = await ubot2.download_media(kontols)
        aku = await tbot.get_me()
        user = aku.first_name
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Hasianmu {user}. Jaga Baik-Baik. Awas Lepas**.",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**GA ADA YANG MAU SAMA LO, MAKANYA GANTENG.**")
