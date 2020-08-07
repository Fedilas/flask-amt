"""empty message

Revision ID: da645ebeb14f
Revises: 4de48c082f15
Create Date: 2020-08-07 09:28:54.942482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da645ebeb14f'
down_revision = '4de48c082f15'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat', 'user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('user', sa.VARCHAR(length=500), nullable=True))
    # ### end Alembic commands ###
