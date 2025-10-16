from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters import Main_menu
from keyboards import daily_routine_kb

router = Router()



@router.message(Main_menu.menu, F.text.endswith("Режим и распорядок"))
async def daily_routine(message: Message, state: FSMContext):

    await message.answer(text="Выберите раздел на клавиатуре ниже", reply_markup=daily_routine_kb())

    await state.set_state(Main_menu.daily_routine)
