
from aiogram import Dispatcher
from aiogram.types import BotCommand

from lexicon.lexicon_ru import LEXICON_COMMANDS_RU

async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [BotCommand(
        command=command,
        description=description) for command, description in LEXICON_COMMANDS_RU.items()]
    await dp.bot.set_my_commands(main_menu_commands)
