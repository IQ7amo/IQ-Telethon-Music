import os

from telethon import Button, events, types
from JE313P.status import *
from JE313P import *


PINS_TEXT = """
**فەرمانەکانی هەڵواسین و سڕینەوەی هەڵواسینی نامە لە گرووپ**
‣ `هەڵواسین `
وەڵامی ئەو نامەیە بدەوە کە دەتەوێت دایبمەزرێنیت
‣ `هەڵگرتنەوە `
وەڵامی ئەو نامەیە بدەوە کە دەتەوێت لایببەی
‣ `سڕینەوەی گشتی `
سڕینەوەی هەموو نامە جێگیرکراوەکان ناو گرووپ
‣ `هەڵواسینن `
بۆ پیشاندانی ئەو نامانەی لە گرووپەکەدا هەڵواسراون
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]نامەی پین کراو"))
async def get_pinned(event):
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await JE313P.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"نامەی هەڵواسراو لە چاتدا{event.chat.title} ئەو <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@JE313P.on(events.NewMessage(pattern="^[!?/]هەڵواسین ?(.*)"))
@is_admin
async def pin(event, perm):
    if not perm.pin_messages:
       await event.reply("پێویستە سەرەتا مۆڵەتی هەڵواسینت هەبێت")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("پێویستە سەرەتا وەڵامی نامەکە بدەیتەوە")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await JE313P.pin_message(event.chat_id, msg, notify=True)
       return
    await JE313P.pin_message(event.chat_id, msg)   

@JE313P.on(events.NewMessage(pattern="^[!?/]سڕینەوەی هەڵواسین ?(.*)"))
@is_admin
async def unpin(event, perm):
    if not perm.pin_messages:
       await event.reply("پێویستە سەرەتا مۆڵەتی هەڵواسینت هەبێت")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await JE313P.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await JE313P.unpin_message(event.chat_id, ok)
    await event.reply(f"بە سەرکەوتوویی لابردنی هەڵواسین[بۆ ئەم نامەیە](t.me/{event.chat.username}/{ok.id}).", link_preview=False)


@JE313P.on(events.NewMessage(pattern="^[!?/]سڕینەوەی گشتی$"))
async def unpinall(event, perm):
    if not perm.pin_messages:
       await event.reply("پێویستە سەرەتا مۆڵەتی هەڵواسینت هەبێت")
       return
    UNPINALL = """
ئایا دڵنیای کە نامەکان هەڵدەگریت ؟
"""

    await JE313P.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("دووپاتکردنەوە", data="unpin")], 
    [Button.inline("هەڵوەشاندنەوە", data="cancel")]])

@JE313P.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await JE313P.unpin_message(event.chat_id)
        await event.edit("بە سەرکەوتوویی هەموو هەڵواسراوەکان هەڵوەشاندرانەوه")
        return 

    await event.answer("پێویستە سەرەتا خاوەنی گروپەکە بیت")

@JE313P.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):

    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("پرۆسەی لابردنی دامەزراندن بۆ هەموو نامەکان هەڵوەشاوەتەوە ")
        return 

    await event.answer("پێویستە سەرەتا خاوەنی گروپەکە بیت")


@JE313P.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("گەڕانەوە", data="help")]])
