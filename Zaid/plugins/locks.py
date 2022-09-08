from telethon import events, Button, types
from Zaid import Zaid
from Zaid.status import *

LOCKS_HELP = """
**ئەمانە فەرمانەکانی داخستن و کردنەوەن لە چاتدا**

داخستن
بۆ داخستنی شتێکی تایبەت لە چاتەکەدا

کردنەوە
بۆ کردنەوەی دەسەڵاتەکان بۆ شتێکی دیاریکراو

دەسەڵاتەکان
بۆ پیشاندانی ئەو دەسەڵاتانەی کە دەتوانیت دایبخەیت
"""

@Zaid.on(events.NewMessage(pattern="^[!?/]داخستن(.*)"))
@is_admin
async def lock(event, perm):
    if not perm.change_info:
      await event.reply("reply("پێویستە مۆڵەتی بەڕێوبەریت هەبێت بۆ بەکارهێنانی ئەم فرمانە")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("تکایە سەرەتا شتێك هەڵبژێرە بۆ ئەوەی دایبخەیت")
       return
    if "نامەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_messages=False)
       await event.reply("- نامەکان داخراوە")
    elif "میدیا" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_media=False)
       await event.reply("- میدیا داخراوە")
    elif "ستیکەرەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_stickers=False)
       await event.reply("- ستیکەرەکان داخراوا.")
    elif "گیفەکان"in input_str:
       await Zaid.edit_permissions(event.chat_id, send_gifs=False)
       await event.reply("- گیف داخراوە")
    elif "ئاڕاستەکردن" in input_str:
       await Zaid.edit_permissions(event.chat_id, forwards=False)
       await event.reply("- ئاڕاستەکردن داخراوە")
    elif "یارییەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_games=False)
       await event.reply("- یارییەکان داخراوە")
    elif "ئینلاین" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_inline=False)
       await event.reply("- ئینلاین داخراوە")
    elif "ده‌نگدان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_polls=False)
       await event.reply("- دەنگدان داخراوە")
    elif "بەستەرەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, embed_link_previews=False)
       await event.reply("- بەستەرەکان داخراوە")
    elif "هەموو" in input_str:
       await Zaid.edit_permissions(event.chat_id,
          send_messages=False, 
          send_media=False,
          send_stickers=False,
          send_gifs=False,
          send_games=False,
          send_inline=False,
          send_polls=False,
          embed_link_previews=False)
       await event.reply("- هەموویان داخراوە")


@Zaid.on(events.NewMessage(pattern="^[!?/]کردنەوە(.*)"))
@is_admin
async def unlock(event, perm):
    if not perm.change_info:
      await event.reply("reply("پێویستە تۆ مۆڵەتی بەڕێوبەریت هەبێت بۆ بەکارهێنانی ئەم فرمانە")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("تکایە سەرەتا شتێک هەڵبژێرە بۆ ئەوەی بیکەیتەوە")
       return
    if "نامەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_messages=True)
       await event.reply("نامەکان کرایەوە")
    elif "میدیا" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_media=True)
       await event.reply("میدیا کرایەوە")
    elif "ستیکەرەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_stickers=True)
       await event.reply("ستیکەرەکان کرایەوە")
    elif "گیفەکان"in input_str:
       await Zaid.edit_permissions(event.chat_id, send_gifs=True)
       await event.reply("گیفەکان کرایەوە")
    elif "ئاڕاستەکردن" in input_str:
       await Zaid.edit_permissions(event.chat_id, forwards=True)
       await event.reply("ئاڕاستەکردن کرایەوە")
    elif "یارییەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_games=True)
       await event.reply("یارییەکان کرایەوە")
    elif "ئینلاین" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_inline=True)
       await event.reply("ئینلاین کرایەوە")
    elif "ده‌نگدان" in input_str:
       await Zaid.edit_permissions(event.chat_id, send_polls=True)
       await event.reply("دەنگدان کرایەوە")
    elif "بەستەرەکان" in input_str:
       await Zaid.edit_permissions(event.chat_id, embed_link_previews=True)
       await event.reply("بەستەرەکان کرایەوە")
    elif "هەموو" in input_str:
       await Zaid.edit_permissions(event.chat_id,
          send_messages=True, 
          send_media=True,
          send_stickers=True,
          send_gifs=True,
          send_games=True,
          send_inline=True,
          send_polls=True,
          embed_link_previews=True)
       await event.reply("هەموویان کرایەوە")


@Zaid.on(events.NewMessage(pattern="^[!?/]دەسەڵاتەکان"))
async def locktypes(event):
    TEXT = """
**Locks:**
‣ نامەکان
‣ میدیا
‣ ستیکەرەکان
‣ گیفەکان
‣ بەستەرەکان
‣ یارییەکان
‣ ئینلاین
‣ ئاڕاستەکردن
‣ ده‌نگدان
‣ هەموو
"""
    await event.reply(TEXT)

@Zaid.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("گەڕانەوە", data="help")]])
