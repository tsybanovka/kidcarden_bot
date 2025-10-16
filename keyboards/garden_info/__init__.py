from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton
from keyboards.functions import load_kb_from_file, keyboards


@keyboards
def create_garden_info_kb() -> ReplyKeyboardMarkup:

    kb = load_kb_from_file("keyboards/garden_info/buttons")

    kb.row(KeyboardButton(text="Назад в меню"))

    return kb.as_markup(resize_keyboard=True)

