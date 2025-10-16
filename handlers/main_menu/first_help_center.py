from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters import Main_menu

router = Router()



@router.message(Main_menu.menu, F.text.endswith("Центр ранней помощи"))
async def fisrt_help_center(message: Message, state: FSMContext):

    await message.answer(text="Гиперссылки на центр")
