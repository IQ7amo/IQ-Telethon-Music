from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("بەڕێوەبەر", data="admin"),],
    [Button.inline("هەڵواسین", data="pins"), Button.inline("پاکردنەوە", data="purges")],
    [Button.inline("کارپێ کردن", data="play"), Button.inline("لابراوەکان", data="zombies")],
    [Button.inline("داخستن", data="locks"), Button.inline("زیاتر", data="misc")],
    [Button.inline("سەرەکی", data="start")]]

HELP_TEXT = "بەخێربێن بۆ لیستی فەرمانەکانی @IQ7amo سەرچاوە\n\nکلیك لە دوگمەکانی خوارەوە بکە:"


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("بۆ بینینی فەرمانەکان کلیك لە خواروە بکە!", buttons=[
       [Button.url("فەرمانەکان و یارمەتی!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
