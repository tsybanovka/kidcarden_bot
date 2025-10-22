from cmath import phase

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.media_group import MediaGroupBuilder

from database import Database_read
from filters import Main_menu
from aiogram.types import Message, FSInputFile

router = Router()

db = Database_read()

@router.message(Main_menu.groups_teachers, F.text.endswith("Младшие группы"))
async def baby_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Младшая группа"]

    if "photos" in data.keys():
        photos = MediaGroupBuilder(caption=data["text"])
        for x in data["photos"]:
            photos.add_photo(media=FSInputFile("database/photos/" + x))

        await message.answer_media_group(caption=data["text"], media=photos.build())
    else:
        await message.answer(text=data["text"])

@router.message(Main_menu.groups_teachers, F.text.endswith("Средние группы"))
async def middle_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Средняя группа"]

    if "photos" in data.keys():
        photos = MediaGroupBuilder(caption=data["text"])
        for x in data["photos"]:
            photos.add_photo(media=FSInputFile("database/photos/" + x))

        await message.answer_media_group(caption=data["text"], media=photos.build())
    else:
        await message.answer(text=data["text"])

@router.message(Main_menu.groups_teachers, F.text.endswith("Старшие группы"))
async def step_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Старшая группа"]

    if "photos" in data.keys():
        photos = MediaGroupBuilder(caption=data["text"])
        for x in data["photos"]:
            photos.add_photo(media=FSInputFile("database/photos/" + x))

        await message.answer_media_group(caption=data["text"], media=photos.build())
    else:
        await message.answer(text=data["text"])

@router.message(Main_menu.groups_teachers, F.text.endswith("Компенсирующие группы"))
async def compens_groups(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Компенсирующая группа"]

    if "photos" in data.keys():
        photos = MediaGroupBuilder(caption=data["text"])
        for x in data["photos"]:
            photos.add_photo(media=FSInputFile("database/photos/" + x))

        await message.answer_media_group(caption=data["text"], media=photos.build())
    else:
        await message.answer(text=data["text"])

@router.message(Main_menu.groups_teachers, F.text.endswith("Педагоги и специалисты"))
async def teachers(message: Message, state: FSMContext):

    data = db.get_groups_teachers()["Педагоги"]

    if "photos" in data.keys():
        photos = MediaGroupBuilder(caption=data["text"])
        for x in data["photos"]:
            photos.add_photo(media=FSInputFile("database/photos/" + x))

        await message.answer_media_group(caption=data["text"], media=photos.build())
    else:
        await message.answer(text=data["text"])