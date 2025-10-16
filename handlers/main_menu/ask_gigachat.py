from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from filters import Main_menu
from keyboards import cancel_kb, main_menu_kb

router = Router()



@router.message(Main_menu.menu, F.text.endswith("Спросить у ИИ"))
async def daily_routine(message: Message, state: FSMContext):

    await message.answer(text="Загрузка...", reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Привет! Готов ответить на все твои вопросы!", reply_markup=cancel_kb)

    await state.set_state(Main_menu.ask_gigachat)

@router.message(Main_menu.ask_gigachat)
async def ask_gigachat(message: Message, state: FSMContext):

    await message.answer(text="пока что я не работаю", reply_markup=cancel_kb)

@router.callback_query(Main_menu.ask_gigachat)
async def back_to_main_menu(data: CallbackQuery, state: FSMContext):

    await data.message.answer(text="Возвращаю в главное меню", reply_markup=main_menu_kb())

    await state.set_state(Main_menu.menu)