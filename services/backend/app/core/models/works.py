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

metadata = MetaData()

works = Table(
    "works",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("workplace_id", Integer, nullable=False),
    Column("deadline", DateTime),
    Column("headline", DateTime, nullable=False),
    Column("description", DateTime),
    Column("creation_date", DateTime, default=func.now(), nullable=False),
    ForeignKeyConstraint(["workplace_id"], [workplaces.c.id], name="works_workplaces_id_fk", ondelete="CASCADE"),
)