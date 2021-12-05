"""Add students table

Revision ID: 96a007d3ee22
Revises: e72c34f78ac2
Create Date: 2021-12-04 15:39:22.513313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96a007d3ee22'
down_revision = 'e72c34f78ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], name='students_class_id_fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='students_users_id_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', name='students_users_id_pk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###