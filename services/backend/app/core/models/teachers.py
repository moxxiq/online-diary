from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Date,
    Table,
    UniqueConstraint,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    ForeignKey,
)
from sqlalchemy.sql import func

from app.core.models.users import users

metadata = MetaData()

teachers = Table(
    "teachers",
    metadata,
    Column("user_id", Integer, nullable=False),
    Column("position", String),
    ForeignKeyConstraint(["user_id"], [users.c.id], name="teachers_users_id_fk", ondelete="CASCADE"),
    PrimaryKeyConstraint("user_id", name='teachers_users_id_pk'),
)