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
    Column('type', Integer,  default=0, nullable=False, comment="1 - admin, 2 - teacher, 3 - student ..."),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('midname', String),
    Column('birthday', Date),
    # SET A NAME. REQUIRED TO THE MIGRATIONS
    # https://alembic.sqlalchemy.org/en/latest/naming.html
)