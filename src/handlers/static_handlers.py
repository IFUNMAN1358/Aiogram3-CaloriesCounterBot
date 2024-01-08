from aiogram import Router, F
from aiogram.types import Message
from src.database.engine import session
from src.database.tables import Users
from src.keyboards.keyboards import start_reply_keyboard

router = Router()

@router.message(F.text == '/start')
async def get_start(message: Message):
    username = message.from_user.username
    user_id = message.from_user.id
    markup = start_reply_keyboard()

    try:
        async with session() as db:
            user = Users(
                user_id=user_id
            )

            db.add(user)
            await db.commit()
        await message.answer(f'Добро пожаловать, {username}.', reply_markup=markup)
    except:
        await message.answer(f'С возвращением, {username}.', reply_markup=markup)