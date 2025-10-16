from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters import Main_menu
from keyboards import reminders_kb

router = Router()



@router.message(Main_menu.menu, F.text.endswith("Напоминалки родителям"))
async def fisrt_help_center(message: Message, state: FSMContext):

    await message.answer(text="Выберите раздел на клавиатуре ниже", reply_markup=reminders_kb())

    await state.set_state(Main_menu.reminders)