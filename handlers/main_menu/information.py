from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters import Main_menu
from keyboards import garden_info_kb

router = Router()


@router.message(Main_menu.menu, F.text.endswith("О садике"))
async def info_about_garden(message: Message, state: FSMContext):

    await message.answer(text="Выберите раздел на клавиатуре ниже", reply_markup=garden_info_kb())

    await state.set_state(Main_menu.information)
