from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command
from answer import resp, just_resp
router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать любую информацию связанную с компанией")


@router.message(Command("just_ask"))
async def message_handler(msg: Message):
    ans = await just_resp(msg.text)
    print(ans)
    await msg.answer(str(ans))


@router.message()
async def message_handler(msg: Message):
    ans = await resp(msg.text)
    print(ans)
    await msg.answer(str(ans))