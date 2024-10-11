from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from answer import resp
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать любую информацию связанную с компанией")


@router.message()
async def message_handler(msg: Message):
    ans = await resp(msg.text)
    print(ans)
    await msg.answer(str(ans))