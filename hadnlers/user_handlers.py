from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import chat_kb
from services.services import get_advice

async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=chat_kb)

async def get_advice_command(message:Message):
    await message.answer(text=LEXICON_RU['processing'])
    await message.answer(text=get_advice())


def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(get_advice_command, text=LEXICON_RU['advice'])
