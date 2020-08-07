"""empty message

Revision ID: 809b54521eb3
Revises: da645ebeb14f
Create Date: 2020-08-07 09:32:45.007186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '809b54521eb3'
down_revision = 'da645ebeb14f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('history')
    op.drop_column('user', 'chat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('chat', sa.VARCHAR(length=120), nullable=True))
    op.create_table('history',
    sa.Column('id', sa.VARCHAR(length=36), nullable=False),
    sa.Column('chat', sa.VARCHAR(length=328), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('chat')
    # ### end Alembic commands ###