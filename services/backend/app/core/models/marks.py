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
    Numeric,
)
from sqlalchemy.sql import func

from app.core.models.works import works
from app.core.models.students import students

metadata = MetaData()

marks = Table(
    "marks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("creation_date", DateTime, nullable=False, default=func.now()),
    Column("comment", String),
    Column("mark", Numeric),
    Column("work_id", Integer, nullable=False),
    Column("student_id", Integer, nullable=False),
    ForeignKeyConstraint(["work_id"], [works.c.id], name="marks_work_id_fk", ondelete="CASCADE"),
    ForeignKeyConstraint(["student_id"], [students.c.user_id], name="marks_student_id_fk", ondelete="CASCADE"),
    UniqueConstraint("work_id", "student_id", name="uq_marks_work_id_student_id")
)