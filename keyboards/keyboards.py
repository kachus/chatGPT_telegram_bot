from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from lexicon.lexicon_ru import LEXICON_RU

chat_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True)

button_advice : KeyboardButton = KeyboardButton(LEXICON_RU['advice'])
button_prediction: KeyboardButton = KeyboardButton(LEXICON_RU['prediction'])
button_question: KeyboardButton = KeyboardButton(LEXICON_RU['my_question'])
chat_kb.add(button_advice).add(button_prediction).add(button_question)
