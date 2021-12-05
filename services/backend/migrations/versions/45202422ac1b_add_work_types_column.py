"""Add work types column

Revision ID: 45202422ac1b
Revises: ca836029635c
Create Date: 2021-12-05 00:17:37.235602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45202422ac1b'
down_revision = 'ca836029635c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('works', sa.Column('work_type_id', sa.Integer(), nullable=False))
    op.create_foreign_key('works_work_types_id_fk', 'works', 'work_types', ['work_type_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('works_work_types_id_fk', 'works', type_='foreignkey')
    op.drop_column('works', 'work_type_id')
    # ### end Alembic commands ###
