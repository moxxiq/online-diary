"""Add workplaces table

Revision ID: d22548ef48be
Revises: 96a007d3ee22
Create Date: 2021-12-04 21:04:42.272174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd22548ef48be'
down_revision = '96a007d3ee22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workplaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], name='workplaces_class_id_fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], name='workplaces_subject_id_fk', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.user_id'], name='workplaces_teacher_id_fk', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('class_id', 'subject_id', 'teacher_id', name='uq_workplaces_class_subject_teacher_ids')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workplaces')
    # ### end Alembic commands ###
