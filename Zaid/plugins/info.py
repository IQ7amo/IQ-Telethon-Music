from telethon import events, Button, types
from Zaid import Zaid
from Zaid.status import *
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
**چەند فەرمانێکی ئاسایی بۆ پیشاندانی ناسنامەی کەسێك**
/Id
ئەم فەرمانە بە وەڵامدانەوە بەکاردێت بۆ پیشاندانی ناسنامە
/info
بۆ پیشاندانی زانیاری بەکارهێنەر بە وەڵامدانەوەی
"""

@Zaid.on(events.NewMessage(pattern="^[!?/]Id"))
async def id(event):

    if event.is_private:
       await event.reply(f"ناسنامەی بەڕێزت🖤 `{event.sender_id}`.")
       return

    ID = """
**ناسنامەی گرووپ :** `{}`
**ناسنامەی بەکارهێنەر :** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"بەکارهێنەر {msg.sender.first_name} /n ناسنامە `{msg.sender_id}`.")
 
@Zaid.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await Zaid(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await Zaid(GetFullUserRequest(event.sender_id))
    text = "**زانیاری بەکارهێنەر:**\n\n"
    text += "**ناوی یەکەم:** {}\n"
    text += "**ناوی دووەم:** {}\n"
    text += "**ئاسنامە:** `{}`\n"
    text += "**ناوی بەکارهێنەر:** @{}\n"
    text += "**ژمارەی وێنەکان:** `{}`\n"
    text += "**بایۆ:** `{}`\n"
    textn += "**بەستەری ئەکاونتەکە:** [کلیك لێرە بکە](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await Zaid.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await Zaid.get_entity(input_str)
    hu = await Zaid(GetFullUserRequest(id=input_str))
    sedd = await Zaid(P(user_id=input_str, offset=42, max_id=0, limit=80))

    text = "**زانیاری بەکارهێنەر:**\n\n"
    text += "**ناوی یەکەم:** {}\n"
    text += "**ناوی دووەم:** {}\n"
    text += "**ناسنامە:** `{}`\n"
    text += "**ناوی بەکارهێنەر:** @{}\n"
    text += "**ژمارەی وێنەکان:** `{}`\n"
    text += "**بایۆ:** `{}`\n"
    textn += "**بەستەری ئەکاونتەکە:** [کلیك لێرە بکە](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   

@Zaid.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("گەڕانەوە", data="help")]])
