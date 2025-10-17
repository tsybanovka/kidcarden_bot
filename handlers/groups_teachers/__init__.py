from aiogram import Router
from handlers.groups_teachers.groups import router as groups


router = Router()


router.include_router(groups)