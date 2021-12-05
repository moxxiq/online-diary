"""Refactor. Add unique constraints

Revision ID: ca836029635c
Revises: 769871c38a82
Create Date: 2021-12-04 23:48:59.660636

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ca836029635c'
down_revision = '769871c38a82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('classes', 'number',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_comment='The year the students went to first grade ')
    op.alter_column('marks', 'creation_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('students', 'class_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('subjects', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'type',
               existing_type=sa.INTEGER(),
               comment='1 - admin, 2 - teacher, 3 - student ...',
               existing_nullable=False)
    op.alter_column('users', 'birthday',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('work_types', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('workplaces', 'class_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('workplaces', 'subject_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('workplaces', 'teacher_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('works', 'workplace_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('works', 'headline',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('works', 'headline',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('works', 'workplace_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('workplaces', 'teacher_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('workplaces', 'subject_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('workplaces', 'class_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('work_types', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'birthday',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('users', 'type',
               existing_type=sa.INTEGER(),
               comment=None,
               existing_comment='1 - admin, 2 - teacher, 3 - student ...',
               existing_nullable=False)
    op.alter_column('subjects', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('students', 'class_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('marks', 'creation_date',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('classes', 'number',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_comment='The year the students went to first grade ')
    # ### end Alembic commands ###