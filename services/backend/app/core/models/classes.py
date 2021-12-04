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

classes = Table(
    "classes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, comment="Belonging to the concrete class among the same year i.e. A, B, C etc."),
    Column("number", Integer, nullable=False, comment="The year the students went to first grade "),
    UniqueConstraint('name', 'number', name="uq_classes_name_number"),
)