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

notes = Table(
    "notes_test",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)