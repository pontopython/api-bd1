from os import remove
from venv import create
from api.users.tui import *
from api.teams.repository import search_members

search_members()