from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton

def load_kb_from_file(path:str) -> ReplyKeyboardBuilder:
    kb = ReplyKeyboardBuilder()

    with open(path, "r", encoding="utf-8") as file:
        data = file.readlines()

    for row in data:
        row = row.replace("\n", "")
        kb.row(*[KeyboardButton(text=x) for x in row.replace("\n", "").split('" "')])

    return kb

def keyboards(func):
    return func