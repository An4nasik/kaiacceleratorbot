import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from decouple import config
token = config("BOT_TOKEN")
ADMIN_ID = config('ADMIN_ID')

from handlers import router


async def main():
    bot = Bot(token)
    dp = Dispatcher(storage=MemoryStorage())
    await bot.set_my_commands([BotCommand(command="just_ask", description="задать вопрос не связанный с компанией")])
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
