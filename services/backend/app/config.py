import re

from decouple import config

DATABASE_URL = config('DATABASE_URL')
# And a special fix for heroku, which update their postgresql config once a lifetime
DATABASE_URL = re.sub(r'^postgres://', r'postgresql://', DATABASE_URL)
SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
FASTAPI_ADMIN_EMAIL = config('FASTAPI_ADMIN_EMAIL')
FASTAPI_ADMIN_PASSWORD = config('FASTAPI_ADMIN_PASSWORD')
