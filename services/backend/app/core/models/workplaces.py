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

from app.core.models.teachers import teachers
from app.core.models.classes import classes
from app.core.models.subjects import subjects

metadata = MetaData()

workplaces = Table(
    "workplaces",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("class_id", Integer, nullable=False),
    Column("subject_id", Integer, nullable=False),
    Column("teacher_id", Integer, nullable=False),
    ForeignKeyConstraint(["class_id"], [classes.c.id], name="workplaces_class_id_fk", ondelete="CASCADE"),
    ForeignKeyConstraint(["subject_id"], [subjects.c.id], name="workplaces_subject_id_fk", ondelete="CASCADE"),
    ForeignKeyConstraint(["teacher_id"], [teachers.c.user_id], name="workplaces_teacher_id_fk", ondelete="CASCADE"),
    UniqueConstraint("class_id", "subject_id", "teacher_id", name="uq_workplaces_class_subject_teacher_ids")
)