"""Add mark values

Revision ID: dabc7a5a5820
Revises: 478b2015ee48
Create Date: 2021-12-13 22:29:52.355139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dabc7a5a5820'
down_revision = '478b2015ee48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('marks', sa.Column('mark', sa.Numeric(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('marks', 'mark')
    # ### end Alembic commands ###