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
    Column("users_id", Integer),
    Column("position", String),
    ForeignKeyConstraint(["users_id"], [users.c.id], name="teachers_users_id_fk", ondelete="CASCADE"),
    PrimaryKeyConstraint("users_id", name='teachers_users_id_pk'),
)