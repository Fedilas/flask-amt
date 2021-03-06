"""empty message

Revision ID: acb89f518ff5
Revises: 6581a9cb6a48
Create Date: 2020-06-10 10:32:44.235320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acb89f518ff5'
down_revision = '6581a9cb6a48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('agreeableness', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('conscientiousness', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('extra', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('neuroticism', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('openness', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'openness')
    op.drop_column('user', 'neuroticism')
    op.drop_column('user', 'extra')
    op.drop_column('user', 'conscientiousness')
    op.drop_column('user', 'agreeableness')
    # ### end Alembic commands ###
