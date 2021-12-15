"""Add mark unique constraint

Revision ID: 1bafcabfb6fd
Revises: dabc7a5a5820
Create Date: 2021-12-13 23:32:52.208326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bafcabfb6fd'
down_revision = 'dabc7a5a5820'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('uq_marks_work_id_student_id', 'marks', ['work_id', 'student_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_marks_work_id_student_id', 'marks', type_='unique')
    # ### end Alembic commands ###
