from handlers import router
from create_bot import dp, bot
import asyncio, logging

logging.basicConfig(level=logging.INFO)

async def start():

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())