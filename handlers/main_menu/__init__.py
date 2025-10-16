from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards import main_menu_kb
from filters import Main_menu, IsBackToMenu

router = Router()



@router.message(CommandStart())
async def start(message: Message, state: FSMContext):

    st = await state.get_state()

    if not st:

        with open("Wellcome_text.txt", "r", encoding="utf-8") as file:
            await message.answer(text="".join(file.readlines()), reply_markup=main_menu_kb())

    else:

        await message.answer(text="Главное меню", reply_markup=main_menu_kb())

        await state.set_state(Main_menu.menu)


@router.message(IsBackToMenu())
async def back_to_menu(message: Message, state: FSMContext):

    await message.answer(text="Возвращаю в главное меню", reply_markup=main_menu_kb())

    await state.set_state(Main_menu.menu)