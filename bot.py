import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import router

load_dotenv()

TOKEN = getenv("TELEGRAM_TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
