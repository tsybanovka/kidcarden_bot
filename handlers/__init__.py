from aiogram import Router
from handlers.main_menu import router as main_menu
from handlers.groups_teachers import router as groups_teachers

router = Router()

router.include_router(main_menu)
router.include_router(groups_teachers)