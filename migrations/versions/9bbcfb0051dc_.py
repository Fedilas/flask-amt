"""empty message

Revision ID: 9bbcfb0051dc
Revises: f703b3fdba55
Create Date: 2020-07-21 23:15:12.663305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9bbcfb0051dc'
down_revision = 'f703b3fdba55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('education', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('experience', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('gender', sa.String(length=120), nullable=True))
    op.add_column('user', sa.Column('nationality', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'nationality')
    op.drop_column('user', 'gender')
    op.drop_column('user', 'experience')
    op.drop_column('user', 'education')
    op.drop_column('user', 'age')
    # ### end Alembic commands ###
