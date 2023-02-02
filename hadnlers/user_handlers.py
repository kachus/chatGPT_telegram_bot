from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (CallbackQuery, Message)
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import chat_kb
from services.services import get_advice, get_prediction, askGPT

user_dict: dict[int, dict[str, str or int]] = {}

class FSMFillForm(StatesGroup):
    fill_question = State() # Состояние ожидания ввода вопроса

async def process_cancel_command(message:Message, state: FSMContext):
    await message.answer(text=LEXICON_RU['/cancel'])
    await state.finish()
    await state.reset_state()

async def process_start_command(message:Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=chat_kb)

async def get_advice_command(message:Message):
    await message.answer(text=LEXICON_RU['processing_advice'])
    await message.reply(text=get_advice())

async def get_prediction_command(message:Message):
    await message.reply(text=LEXICON_RU['processing_prediction'])
    await message.reply(text=get_prediction())

async def process_question_pressed(message:Message):
    await message.reply(text=LEXICON_RU['ask_question'])
    await FSMFillForm.fill_question.set()

async def process_getback_response(message:Message, state: FSMContext):
    if message.text == '/cancel':
        return await process_cancel_command(message, state)
    '''''
    #keeping user's info in data dict 
    async with state.proxy() as data:
        data['user_question'] = message.text
    user_dict[message.from_user.id] = await state.get_data()
    '''''
    await message.reply(text=askGPT(message.text))


def register_user_handlers(dp:Dispatcher):
    dp.register_message_handler(process_start_command, commands='start')
    dp.register_message_handler(get_advice_command, text=LEXICON_RU['advice'])
    dp.register_message_handler(get_prediction_command, text=LEXICON_RU['prediction'])
    dp.register_message_handler(process_question_pressed, text=LEXICON_RU['my_question'])
    dp.register_message_handler(process_getback_response, state=FSMFillForm.fill_question),
    dp.register_message_handler(process_cancel_command, commands='cancel')
