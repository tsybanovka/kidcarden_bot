from aiogram import Router
from handlers.main_menu import router as main_menu

router = Router()

router.include_router(main_menu)