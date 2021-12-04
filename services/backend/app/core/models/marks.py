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

from app.core.models.workplaces import workplaces
from app.core.models.students import students

metadata = MetaData()

marks = Table(
    "marks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("creation_date", DateTime, nullable=False, default=func.now()),
    Column("comment", String),
    Column("workplace_id", Integer, nullable=False),
    Column("student_id", Integer, nullable=False),
    ForeignKeyConstraint(["workplace_id"], [workplaces.c.id], name="marks_workplace_id_fk", ondelete="CASCADE"),
    ForeignKeyConstraint(["student_id"], [students.c.user_id], name="marks_student_id_fk", ondelete="CASCADE"),
)