from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU

chat_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True)

button_advice : KeyboardButton = KeyboardButton(LEXICON_RU['advice'])
button_prediction: KeyboardButton = KeyboardButton(LEXICON_RU['prediction'])
button_question: KeyboardButton = KeyboardButton(LEXICON_RU['my_question'])
#buttin_question doesn't work in group chats

chat_kb.add(button_advice).add(button_prediction)



inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()

button_advice_inl: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['advice'], callback_data='advice_bt_pressed')
button_prediction_inl: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['prediction'], callback_data='prediction_bt_pressed')
button_question_inl: InlineKeyboardButton = InlineKeyboardButton(text=LEXICON_RU['my_question'], callback_data='question_bt_pressed')

inline_kb.add(button_advice_inl).add(button_prediction_inl).add(button_question_inl)