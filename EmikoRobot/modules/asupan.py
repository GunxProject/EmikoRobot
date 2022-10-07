# 🍀 © @tofik_dn
# ⚠️ Do not remove credits

import random

from EmikoRobot.events import register
from EmikoRobot import telethn as tbot, ubot2

from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterMusic
from telethon.tl.types import InputMessagesFilterPhotos


@register(pattern="^/Asupan(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari Video Asupan (Bermanfaat) Dulu...**")
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@renunganbarengg", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Nih Asupan Bermanfaatnya... Semoga Harimu Indah...**",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan video...**")


@register(pattern="^/lagurohani(.*)")
async def _(event):
    memek = await event.reply("**🔍 Mencari Lagu Rohani Dulu...**")
    try:
        desahannya = [
            desah
            async for desah in ubot2.iter_messages(
            "@lagurohanikristen", filter=InputMessagesFilterMusic
            )
        ]
        kontols = random.choice(desahannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat_id,
            caption=f"**Silahkan Di dengarkan. Tuhan Memberkati Kamu. Amin **",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan lagu rohaninya. 😭.**")


@register(pattern="^/cowokku(.*)")
async def _(event):
    memek = await event.reply("**🔍 Bentar ya.. Batee lagi cari cowok untukmu...**")
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
            caption=f"**Nih cowok untukmu, moga kalian jodoh.**",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**Tidak dapat menemukan cowok untukmu. Mungkin belum lahir. Sabar ya.**")


@register(pattern="^/cewekku(.*)")
async def _(event):
    memek = await event.reply("**🔍 Bentar ya batee lagi Cari cewek untukmu...**")
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
            caption=f"**Nih cewek untukmu. Langsung gass...**.",
            file=pantek
            )
        await memek.delete()
    except Exception:
        await memek.edit("**GA ADA CEWEK UNTUKMU BAH, MAKANYA GANTENG.**")
