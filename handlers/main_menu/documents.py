from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters import Main_menu
from keyboards import documents_kb

router = Router()



@router.message(Main_menu.menu, F.text.endswith("Документы для родителей"))
async def documents(message: Message, state: FSMContext):

    await message.answer(text="Выберите раздел на клавиатуре ниже", reply_markup=documents_kb())

    await state.set_state(Main_menu.documents)
