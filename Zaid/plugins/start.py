from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
🕷️🖤 بەخێربێیت بەڕێزم{}!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘
‣ من بۆتێکی سادەم بۆ پاراستنی گروپەکەت و پەخشکردنی کلیپی دەنگی لە پەیوەندییەکدا.
‣ دەتوانم کلیپی دەنگی لە کاتی پەیوەندیدا لێبدەم.
‣ دەتوانم هەر بەکارهێنەرێک بلۆک بکەم و بێدەنگ بکەم.
‣ باشترین بۆت لە ڕووی تایبەتمەندییەوە.
‣ بۆتەکە خێرایە دروستکراوی کتێبخانەی IQ7amo یە
‣ کاتێکی خۆش بەسەر بەرە لەگەڵ بۆتەکە
        🖤🥰
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ ** بەهیوای کاتێکی خۆش بەسەر بەریت لەگەڵ بۆتەکە**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name),  buttons=[
        [Button.url("➕ بۆ زیادکردنم ئێرە دابگرە", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👾 خاوەنی بۆت", "https://t.me/IQ7amo")],
        [Button.url("🗣️ پشتگیری", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 کەناڵ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("فەرمانەکان", data="help")]])
       return

    if event.is_group:
       await event.reply("**بە سەرکەوتوویی کاردەکەم**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ بۆ زیادکردنم ئێرە دابگرە", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👾 خاوەنی بۆت", "https://t.me/IQ7amo")],
        [Button.url("🗣️ پشتگیری", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 کەناڵ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("فەرمانەکان", data="help")]])
       return
