from keyboards.functions import keyboards
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup, InlineKeyboardBuilder


@keyboards
def create_cancel_kb() -> InlineKeyboardMarkup:

    kb = InlineKeyboardBuilder()

    kb.row(InlineKeyboardButton(text="Назад", callback_data="cancel"))

    return kb.as_markup()