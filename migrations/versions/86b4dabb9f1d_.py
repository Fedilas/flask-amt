"""empty message

Revision ID: 86b4dabb9f1d
Revises: 3400609f8c2f
Create Date: 2020-08-07 10:09:14.924356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86b4dabb9f1d'
down_revision = '3400609f8c2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('chat', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('message', 'chat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('chat', sa.VARCHAR(length=140), nullable=True))
    op.drop_table('chat')
    # ### end Alembic commands ###
