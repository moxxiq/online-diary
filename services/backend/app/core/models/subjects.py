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

subjects = Table(
    "subjects",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    UniqueConstraint('name', name="uq_subjects_name"),
)