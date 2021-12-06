from app.config import DATABASE_URL
from decouple import config
from sqlalchemy import create_engine
from databases import Database


# SQLAlchemy
engine = create_engine(DATABASE_URL)

# databases query builder
database = Database(DATABASE_URL)
