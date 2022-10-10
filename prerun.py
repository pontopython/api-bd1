from api.users import create_user_interactively, save_user_to_file
from api.utils import create_empty_data_if_needed

create_empty_data_if_needed()
create_user_interactively(prerun=True)
