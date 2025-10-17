from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from filters import Main_menu
from keyboards import cancel_kb

router = Router()



@router.message(Main_menu.menu, F.text.endswith("Сотрудникам"))
async def employee(message: Message, state: FSMContext):

    await message.answer(text="Загрузка...", reply_markup=ReplyKeyboardRemove())
    await message.answer(text="Введите свой логин", reply_markup=cancel_kb)

    await state.set_state(Main_menu.employee)


@router.callback_query(Main_menu.employee, F.data == "cancel")
async def go_back_to_the_main_menu(data: CallbackQuery, state: FSMContext):

    await data.message.answer(text="Возвращаю в главное меню")

    await state.set_state(Main_menu.menu)