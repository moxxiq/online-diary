from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Date,
    Table,
    UniqueConstraint,
)
from sqlalchemy.sql import func

metadata = MetaData()

work_type = Table(
    "work_type",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("work_type", String),
    UniqueConstraint('work_type', name="uq_work_type"),
)