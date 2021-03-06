"""empty message

Revision ID: 21c8bf9b9e5b
Revises: 0311421b52fb
Create Date: 2020-05-23 08:47:24.043017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '21c8bf9b9e5b'
down_revision = '0311421b52fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('city')
    op.add_column('user', sa.Column('ability', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'ability')
    op.create_table('city',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('state', sa.VARCHAR(length=2), nullable=True),
    sa.Column('name', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
