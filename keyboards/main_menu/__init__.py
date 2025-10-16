from aiogram.utils.keyboard import ReplyKeyboardBuilder, ReplyKeyboardMarkup, KeyboardButton



def create_main_menu_kb() -> ReplyKeyboardMarkup:

    kb = ReplyKeyboardBuilder()

    with open("keyboards/main_menu/buttons", "r", encoding="utf-8") as file:
        data = file.readlines()

    for row in data:
        row = row.replace("\n", "")
        kb.row(*[KeyboardButton(text=x) for x in row.replace("\n", "").split('" "')])

    return kb.as_markup(resize_keyboard=True)