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
from app.core.models.classes import classes

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("user_id", Integer, nullable=False),
    Column("class_id", Integer, nullable=False),
    ForeignKeyConstraint(["user_id"], [users.c.id], name="students_users_id_fk", ondelete="CASCADE"),
    ForeignKeyConstraint(["class_id"], [classes.c.id], name="students_class_id_fk", ondelete="CASCADE"),
    PrimaryKeyConstraint("user_id", name='students_users_id_pk'),
)