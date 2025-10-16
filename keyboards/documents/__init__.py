from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton
from keyboards.functions import load_kb_from_file, keyboards


@keyboards
def create_documents_kb() -> ReplyKeyboardMarkup:

    kb = load_kb_from_file("keyboards/documents/buttons")

    kb.row(KeyboardButton(text="Назад в меню"))

    return kb.as_markup(resize_keyboard=True)