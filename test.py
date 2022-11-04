from api.users.common import USER_TYPES
from api.evaluations.tui import admin_create_evaluation
from api.new_main import admin_main
from api.users.repository import create_user, get_user_by_id, get_users
from api.users.tui import admin_create_a_new_user, summary_user
admin_main()