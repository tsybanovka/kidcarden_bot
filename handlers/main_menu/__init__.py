from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards import main_menu_kb
from filters import Main_menu, IsBackToMenu

from handlers.main_menu.information import router as information
from handlers.main_menu.daily_routine import router as daily_routine
from handlers.main_menu.service import router as service
from handlers.main_menu.documents import router as documents
from handlers.main_menu.first_help_center import router as first_help_center
from handlers.main_menu.reminders import router as reminders
from handlers.main_menu.ask_gigachat import router as ask_question

router = Router()

router.include_router(information)
router.include_router(daily_routine)
router.include_router(service)
router.include_router(documents)
router.include_router(first_help_center)
router.include_router(reminders)
router.include_router(ask_question)


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
