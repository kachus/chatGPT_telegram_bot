import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from hadnlers.user_handlers import register_user_handlers

logger = logging.getLogger(__name__)

def register_all_handlers(dp:Dispatcher) -> None:
    register_user_handlers(dp)


async def main():
    # logging config
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')

    # info about starting the bot
    logger.info('Starting bot')

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await bot.close


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Выводим в консоль сообщение об ошибке,
        # если получены исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')