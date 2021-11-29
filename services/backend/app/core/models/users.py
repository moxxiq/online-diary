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
)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String, unique=True, nullable=False),
    Column('hashed_password', String(64), nullable=False),
    Column('type', Integer, nullable=False),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('midname', String),
    Column('birthday', Date, nullable=False),
    # SET A NAME. REQUIRED TO THE MIGRATIONS
    # https://alembic.sqlalchemy.org/en/latest/naming.html
    UniqueConstraint('name', 'surname', 'midname', 'birthday', name="uq_users_name_surname_midname_birthday"),
)