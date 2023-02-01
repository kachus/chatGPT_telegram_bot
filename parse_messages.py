
import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Initialize bot and dispatcher
bot = Bot(token="<bot_token>")
dp = Dispatcher(bot)

# Create a dict to store user's channels and keywords
user_channels = {}

# Handle '/start' command
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.reply("Hi! I'm a telegram bot and I can track updates in channels.\nTo start tracking a channel, send me its ID and then type the keywords you want to track.")

# Handle channel id
@dp.message_handler()
async def channel_handler(message: types.Message):
    # Check if the message contains a valid channel id
    if message.text.startswith("@"):
        # Store the user's channel and keywords
        user_channels[message.from_user.id] = {
            "channel_id": message.text,
            "keywords": []
        }
        await message.reply("Channel ID successfully added. Now type the keywords you want to track.")

# Handle keywords
@dp.message_handler()
async def keyword_handler(message: types.Message):
    # Get the user's channel and keywords
    user_data = user_channels.get(message.from_user.id)
    # Check if the user has sent a channel id
    if user_data is not None:
        # Store the user's keywords
        user_data["keywords"].append(message.text)
        await message.reply("Keyword successfully added. You can add more keywords or type /stop to finish.")

# Handle '/stop' command
@dp.message_handler(commands=['stop'])
async def stop_handler(message: types.Message):
    # Get the user's channel and keywords
    user_data = user_channels.get(message.from_user.id)
    # Check if the user has sent a channel


