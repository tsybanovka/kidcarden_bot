from aiogram.fsm.state import StatesGroup, State


class Main_menu(StatesGroup):

    menu = State()
    information = State()
    groups_teachers = State()
    daily_routine = State()
    first_help_center = State()
    documents = State()
    reminders = State()
    ask_gigachat = State()
    employee = State()
    service = State()