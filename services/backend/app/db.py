from decouple import config
from sqlalchemy import create_engine
from databases import Database

DATABASE_URL = config('DATABASE_URL')

# SQLAlchemy
engine = create_engine(DATABASE_URL)

# databases query builder
database = Database(DATABASE_URL)
