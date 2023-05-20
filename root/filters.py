from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    key = 'admin'

    def __init__(self, admin):
        self.admin = admin

    async def check(self, message: types.Message):
        member = await message.bot.get_chat_member(message.chat.id, message.from_user.id)
        return member.is_chat_admin()


class ReplyFilter(BoundFilter):
    key = 'reply'

    async def check(self, message: types.Message):
        try:
            if message.reply_to_message.from_user.id == message.bot.id:
                return True
        except AttributeError:
            pass
