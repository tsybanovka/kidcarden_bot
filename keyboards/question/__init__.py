from keyboards.functions import keyboards
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardBuilder


@keyboards
def create_question_kb() -> ReplyKeyboardMarkup:

    kb = ReplyKeyboardBuilder()

    kb.row(KeyboardButton(text="Да"), KeyboardButton(text="Нет"))
    kb.row(KeyboardButton(text="Назад в меню"))

    return kb.as_markup(resize_keyboard=True)