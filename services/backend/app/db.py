import enum
from decouple import config

from app.core.schemas.users import UserType

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Enum,
    Date,
    Table,
    UniqueConstraint,
    create_engine
)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = config('DATABASE_URL')

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "notes_test",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, unique=True, nullable=False),
    Column('password', String(64), nullable=False),
    Column('type', Enum(UserType), nullable=False),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('midname', String),
    Column('birthday', Date),
    UniqueConstraint('name', 'surname', 'midname', 'birthday'),
)


# databases query builder
database = Database(DATABASE_URL)
