from aiogram import Bot, Dispatcher
from asyncio import*
from os import*
from dotenv import load_dotenv
from src.database.engine import engine, session
from src.database.tables import Base
from src.handlers import static_handlers
from src.handlers import dynamic_handlers
from src.keyboards import callbacks

load_dotenv()

async def start():
    bot = Bot(token=environ.get("TOKEN"))
    dp = Dispatcher()

    dp.include_routers(static_handlers.router,
                       dynamic_handlers.router,
                       callbacks.router)

    db = session()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        await db.close()

if __name__ == "__main__":
    run(start())







