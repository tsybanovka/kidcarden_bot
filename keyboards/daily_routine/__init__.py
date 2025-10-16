from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardBuilder
from keyboards.functions import load_kb_from_file, keyboards

@keyboards
def create_daily_routine_kb() -> ReplyKeyboardMarkup:

    kb = load_kb_from_file("keyboards/daily_routine/buttons")

    kb.row(KeyboardButton(text="Назад в меню"))

    return kb.as_markup(resize_keyboard=True)