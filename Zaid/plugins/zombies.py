from telethon import events, Button
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from JE313P import JE313P
from JE313P.status import *


CLEANER_HELP = """
**فەرمانەکانن بۆ پیشاندان و سڕینەوەی ئەکاونتە سڕاوەکان**
/deleted
بۆ بینینی ئەکاونتە سڕاوەکان لە چاتدا

/clear
بۆ سڕینەوە و دەرکردنی ئەکاونتە سڕاوەکان لە گرووپدا

"""


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@JE313P.on(events.NewMessage(pattern="^[!?/]سڕاوەکان ?(.*)"))
@is_admin
async def clean(event, perm):
    if not perm.ban_users:
      await event.reply("- تۆ مۆڵەتی پێویستت نییە")
      return
    input_str = event.pattern_match.group(1)
    stats = "گرووپەکە خاوێنە"
    deleted = 0

    if "clean" not in input_str:
      zombies = await event.respond("بەدوای ئەو ئەکاونتانەدا دەگەڕێت کە سڕاونەتەوە یان دوایین جار بینراون کە کۆنن")
      async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                deleted += 1
      if deleted > 0:
            stats = f".دۆزرایەوە **{deleted}** سڕاوەکان لێره\
            \nبۆ دەرکردنیان بنێرن `/سڕاوەکان پاکه`"
      await zombies.edit(stats)
      return

    cleaning_zombies = await event.respond("- ئەکاونتە سڕاوەکان دەردەکرێن، کەمێك چاوەڕێ بکە")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_zombies.edit("- ببوورە مۆڵەتی تەواوم نییە بۆ ئەم فەرمانە")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        stats = f"پاکراوەتەوە`{del_u}` لە ئەکاونتە سڕاوەکانەوە"

    if del_a > 0:
        stats = f"پاکراوەتەوە`{del_u}` لە ئەکاونتە سڕاوەکانەوە \
        \n`{del_a}` ئەکاونتە سڕاوەکانی ئەدمین دەرنەکراون"

    await cleaning_zombies.edit(stats)

@JE313P.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("گەڕانەوە", data="help")]])
