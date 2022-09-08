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

@Zaid.on(events.NewMessage(pattern="^[!?/]auth(.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("ئەم فەرمانە تەنیا لە گرووپدا بەکاردێت")
       return

    if not perm.add_admins:
        await event.reply("پێوستە مۆڵەتی بلۆککردنت هەبێت بۆ بەکارهێنانی ئەم فەمانە")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("پێویستە وەڵامی بەکارهێنەر بدەیتەوە بۆ ئەوەی بەرزی بکاتەوە")
        return
    sed = await Zaid(GetFullUserRequest(id=user.sender_id or input_str))
    await Zaid(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=True,
                    change_info=False,
                    ban_users=True,
                    delete_messages=True,
                    pin_messages=True), rank="Admin"))

    if not input_str:
        await event.reply(f"- بە سەرکەوتوویی بەرزکرایەوە [{sed.user.first_name}](tg://user?id={user.sender_id}) لە {event.chat.title}!")
        return

    await event.reply(f"بەکارهێنەرەکە بە سەرکەوتوویی بەرزکرایەوە {input_str} in {event.chat.title}")
 
@Zaid.on(events.NewMessage(pattern="^[!?/]unauth (.*)"))
@is_admin
async def promote(event, perm):
    if event.is_private:
       await event.reply("ئەم فرمانە تەنیا لە گرووپدا بەکاردێت")
       return
    if not perm.add_admins:
        await event.reply("پێویستە مۆڵەتی بلۆککردنت هەبێت بۆ بەکارهێنانی ئەم فەرمانە")
        return
    input_str = event.pattern_match.group(1)
    user = await event.get_reply_message()
    if not input_str and not user:
        await event.reply("پێویستە وەڵامی ئەو بەکارهێنەرە بدەیتەوە کە دەتەوێت دایبەزێنیت")
        return
    sed = await Zaid(GetFullUserRequest(id=user.sender_id or input_str))
    await Zaid(EditAdminRequest(event.chat_id, user.sender_id or input_str, ChatAdminRights(
                    add_admins=False,
                    invite_users=None,
                    change_info=None,
                    ban_users=None,
                    delete_messages=None,
                    pin_messages=None), rank="Not Admin"))

    if not input_str:
        await event.reply(f"- بە سەرکەوتوویی دابەزێنراوە[{sed.user.first_name}](tg://user?id={user.sender_id}) له {event.chat.title}!")
        return

    await event.reply(f"- بە سەرکەوتوویی دابەزێنراوە {input_str} in {event.chat.title}")
 

@JE313P.on(events.NewMessage(pattern="^[!?/]link"))
async def invitelink(event):

    if event.is_private:
       await event.reply("ئەم فرمانە تەنیا لە گرووپدا بەکاردێت")
       return
    link = await Zaid(ExportChatInviteRequest(event.chat_id))
    await event.reply(f"گرووپەکە {event.chat.title}بەستەر: [کلیك لێرە بکە]({link.link})", link_preview=False)


ADMIN_TEXT = """
**✘ تەنیا بەڕێوبەرەکان دەتوانن ئەم فەرمانانە بەکاربهێنن**

‣ `/stop` - بۆ کۆتایی هاتنی پەخشکردن.
‣ `/skip` - بۆ تێپەڕاندنی پەخشکراو.
‣ `/pause` - بۆ وەستاندنی پەخشکردن.
‣ `/resume` - بۆ دەستپێکردنەوەی پەخشکردن.
‣ `/leave` - بۆ جێهێشتنی ناچاری.
‣ `/playlist` -  بۆ بینینی لیستی پەخشکراوەکان.
‣ `/auth` - بۆ بەرزکردنەوەی مۆڵەتی بەڕێوبەری.
‣ `/unauth` - بۆ دابەزاندنی مۆڵەتی بەڕێوبەری بە وەڵام دانەوەی ئەو کەسەی دەتەوێ.
‣ `/link` - بۆ پیشاندانی بەستەری گرووپ لە چاتەکەدا.
"""

PLAY_TEXT = """
**✘ فەرمانە ئاساییەکانی بەکارهێنەر**

‣ `/play` - بۆ پەخشکردنی کلیپی دەنگی
‣ `/vplay` - بۆ پەخشکردنی ڤیدیۆ (HEROKU_MODE > Doesn't support).
"""
