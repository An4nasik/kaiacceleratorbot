import datetime
import sqlite3

from data.users import Messages
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from answer import resp, just_resp
from data import db_session
from sqlalchemy import text
con = sqlite3.connect("users.db", check_same_thread=False)
cur = con.cursor()
db_session.global_init("db/users.db")
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
    ans, req = await just_resp(message.text)
    print("ans: ", ans)
    print("req: ", req)
    while not ans:
        ans, req = await just_resp(message.text)
    post = Messages(id=message.from_user.id, message=("Запрос - " + req + " Ответ - " + ans + " Дата - " + str(datetime.datetime.now())))
    db_sess = db_session.create_session()
    db_sess.add(post)
    db_sess.commit()
    db_sess.close()
    await state.clear()
    await message.reply(ans)



@router.message()
async def message_handler(msg: Message):
    ans = await resp(msg.text)
    print("ans: ", ans)
    while not ans:
        ans = await resp(msg.text)
    post = Messages(id=msg.from_user.id, message=("Запрос - " + msg.text + " Ответ - " + ans + " Дата - " + str(datetime.datetime.now())))
    db_sess = db_session.create_session()
    db_sess.add(post)
    db_sess.commit()
    db_sess.close()
    await msg.answer(str(ans))
