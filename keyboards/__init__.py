from keyboards.main_menu import create_main_menu_kb
from keyboards.garden_info import create_garden_info_kb
from keyboards.groups_teachers import create_groups_teachers_kb
from keyboards.daily_routine import create_daily_routine_kb
from keyboards.documents import create_documents_kb
from keyboards.reminders import create_reminders_kb
from keyboards.cancel import create_cancel_kb


main_menu_kb = create_main_menu_kb
garden_info_kb = create_garden_info_kb
groups_teachers_kb = create_groups_teachers_kb
daily_routine = create_daily_routine_kb()
documents_kb = create_documents_kb
reminders_kb = create_reminders_kb
cancel_kb = create_cancel_kb()