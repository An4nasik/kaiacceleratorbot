from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.filters import Command
from answer import resp, just_resp
router = Router()

class Form(StatesGroup):
    data = State()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу тебе узнать любую информацию связанную с компанией")


@router.message(Command("just_ask"))
async def message_handler(msg: Message, state: FSMContext):
    await state.set_state(Form.data)
    await msg.reply("Ожидаю ваш запрос")

@router.message(Form.data)
async def process_name(message: types.Message, state: FSMContext):
    # Finish our conversation
    print(message.text)
    ans, req = await just_resp(message.text)
    print(req)
    await state.clear()
    await message.reply(ans)

@router.message()
async def message_handler(msg: Message):
    ans = await resp(msg.text)
    print(ans)
    await msg.answer(str(ans))


