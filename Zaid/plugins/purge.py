from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
import time

PR_HELP = """
**✘ ئەمە لیستی فەرمانەکانی پاککردنەوەیە تایبەتە بەمن
‣ `/clear`
بە وەڵامدانەوەی نامەیەك بۆ پاککردنەوەی
‣ `/delet`
وەڵامی نامەیەك بدەرەوە بۆ سڕینەوەی
"""

@Zaid.on(events.NewMessage(pattern=r"^[?!]clear"))
@is_admin
async def purge_messages(event, perm):
    if not perm.delete_messages:
         await event.reply("سەرەتا پێویستت بە مۆڵەتی سڕینەوەیە")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "پێویستە لە خوارەوە وەڵامی ئەو نامەیە بدەیتەوە کە دەتەوێت بیسڕیتەوە")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"پاککراوەتەوە لە {time_:0.2f} لە چرکە"
    await event.respond(text, parse_mode='markdown')



@Zaid.on(events.NewMessage(pattern="^[!?/]delet$"))
@is_admin
async def delete_messages(event, perm):
    if not perm.delete_messages:
       await event.reply("- سەرەتا پێویستت بە مۆڵەتی سڕینەوەیە")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("پێویستە وەڵامی ئەو نامەیە بدەیتەوە کە دەیسڕیتەوە")
      return

    await msg.delete()
    await event.delete()

@Zaid.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("گەڕانەوە", data="help")]])
