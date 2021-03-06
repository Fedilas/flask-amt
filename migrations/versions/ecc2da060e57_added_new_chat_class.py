"""added new chat class

Revision ID: ecc2da060e57
Revises: 72b96cce04da
Create Date: 2020-08-06 18:57:39.205430

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecc2da060e57'
down_revision = '72b96cce04da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('chat', sa.String(length=328), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_chat_timestamp', table_name='chat')
    op.drop_table('chat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), nullable=True),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('language', sa.VARCHAR(length=5), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_chat_timestamp', 'chat', ['timestamp'], unique=False)
    op.drop_table('history')
    # ### end Alembic commands ###
