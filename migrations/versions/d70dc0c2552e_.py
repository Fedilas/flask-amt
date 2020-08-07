"""empty message

Revision ID: d70dc0c2552e
Revises: ecc2da060e57
Create Date: 2020-08-06 22:13:26.778858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd70dc0c2552e'
down_revision = 'ecc2da060e57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'chat')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('chat', sa.VARCHAR(length=120), nullable=True))
    # ### end Alembic commands ###
