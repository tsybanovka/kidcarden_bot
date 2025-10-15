from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage import redis

bot = Bot(token=config("API_TOKEN"), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher(storage=redis.RedisStorage.from_url(config("REDIS_URL")))