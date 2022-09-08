from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« گەڕانەوە", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« گەڕانەوە", data="help")]])


ADMIN_TEXT = """
**✘ تەنیا بەڕێوبەرەکان دەتوانن ئەم فەرمانانە بەکاربهێنن**

‣ `/stop` - بۆ کۆتایی هاتنی پەخشکردن
‣ `/skip` - بۆ تێپەڕاندنی پەخشکراو
‣ `/pause` - بۆ وەستاندنی پەخشکردن
‣ `/resume` - بۆ دەستپێکردنەوەی پەخشکردن
‣ `/leavevc` - جێهێشتنی ناچاری.
‣ `/playlist` - لیستی پەخشکراوەکان.
"""

PLAY_TEXT = """
**✘ فەرمانە ئاساییەکانی بەکارهێنەر**

‣ `/play` - بۆ پەخشکردنی کلیپی دەنگی
‣ `/vplay` - بۆ پەخشکردنی ڤیدیۆ (HEROKU_MODE > Doesn't support).
"""
