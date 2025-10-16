from aiogram.filters import BaseFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


class IsBackToMenu(BaseFilter):

    def __call__(self, message: Message, state: FSMContext):

        if message.text == "Назад в меню":

            return True

        return False