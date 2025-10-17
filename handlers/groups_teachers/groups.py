from cmath import phase

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from database import Database_read
from filters import Main_menu
from aiogram.types import Message, FSInputFile, InputMediaPhoto

router = Router()

db = Database_read()

@router.message(Main_menu.groups_teachers, F.text.endswith("Младшие группы"))
async def baby_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Младшая группа"]

    photos = data["photos"]
    photos = list(map(lambda x: InputMediaPhoto(media=FSInputFile("database/photos/" + x)), photos))

    await message.answer_media_group(caption=data["text"], media=photos)

@router.message(Main_menu.groups_teachers, F.text.endswith("Средние группы"))
async def middle_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Средняя группа"]

    photos = data["photos"]
    photos = list(map(lambda x: InputMediaPhoto(media=FSInputFile("database/photos/" + x)), photos))

    await message.answer_media_group(caption=data["text"], media=photos)

@router.message(Main_menu.groups_teachers, F.text.endswith("Старшие группы"))
async def step_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Старшая группа"]

    photos = data["photos"]

    photos = list(map(lambda x: InputMediaPhoto(media=FSInputFile("database/photos/"+x)), photos))
    print(photos)

    await message.answer_media_group(caption=data["text"], media=photos)

@router.message(Main_menu.groups_teachers, F.text.endswith("Компенсирующие группы"))
async def compens_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Компенсирующая группа"]

    photos = data["photos"]
    photos = list(map(lambda x: InputMediaPhoto(media=FSInputFile("database/photos/" + x)), photos))

    await message.answer_media_group(caption=data["text"], media=photos)

