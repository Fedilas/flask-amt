"""empty message

Revision ID: 8386a33ced5b
Revises: 58ef19897e12
Create Date: 2020-08-15 09:57:32.251689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8386a33ced5b'
down_revision = '58ef19897e12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('room', sa.String(length=140), nullable=True),
    sa.Column('user', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_timestamp'), 'chat', ['timestamp'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('amt_id', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('extra', sa.String(length=120), nullable=True),
    sa.Column('trust', sa.String(length=120), nullable=True),
    sa.Column('lazy', sa.String(length=120), nullable=True),
    sa.Column('relax', sa.String(length=120), nullable=True),
    sa.Column('art', sa.String(length=120), nullable=True),
    sa.Column('social', sa.String(length=120), nullable=True),
    sa.Column('fault', sa.String(length=120), nullable=True),
    sa.Column('job', sa.String(length=120), nullable=True),
    sa.Column('nervous', sa.String(length=120), nullable=True),
    sa.Column('imagination', sa.String(length=120), nullable=True),
    sa.Column('ability', sa.String(length=120), nullable=True),
    sa.Column('extraversion', sa.String(length=120), nullable=True),
    sa.Column('agreeableness', sa.String(length=120), nullable=True),
    sa.Column('conscientiousness', sa.String(length=120), nullable=True),
    sa.Column('neuroticism', sa.String(length=120), nullable=True),
    sa.Column('openness', sa.String(length=120), nullable=True),
    sa.Column('match', sa.String(length=120), nullable=True),
    sa.Column('role', sa.String(length=120), nullable=True),
    sa.Column('code', sa.String(length=120), nullable=True),
    sa.Column('gender', sa.String(length=120), nullable=True),
    sa.Column('age', sa.String(length=120), nullable=True),
    sa.Column('nationality', sa.String(length=120), nullable=True),
    sa.Column('education', sa.String(length=120), nullable=True),
    sa.Column('experience', sa.String(length=120), nullable=True),
    sa.Column('performance', sa.String(length=120), nullable=True),
    sa.Column('cohesion', sa.String(length=120), nullable=True),
    sa.Column('communication', sa.String(length=120), nullable=True),
    sa.Column('balance', sa.String(length=120), nullable=True),
    sa.Column('balance_extra', sa.String(length=120), nullable=True),
    sa.Column('comments', sa.String(length=120), nullable=True),
    sa.Column('improve', sa.String(length=120), nullable=True),
    sa.Column('keep', sa.String(length=120), nullable=True),
    sa.Column('other', sa.String(length=120), nullable=True),
    sa.Column('enthusiasm', sa.String(length=120), nullable=True),
    sa.Column('critical', sa.String(length=120), nullable=True),
    sa.Column('dependable', sa.String(length=120), nullable=True),
    sa.Column('anxious', sa.String(length=120), nullable=True),
    sa.Column('complex', sa.String(length=120), nullable=True),
    sa.Column('reserved', sa.String(length=120), nullable=True),
    sa.Column('warm', sa.String(length=120), nullable=True),
    sa.Column('careless', sa.String(length=120), nullable=True),
    sa.Column('calm', sa.String(length=120), nullable=True),
    sa.Column('uncreative', sa.String(length=120), nullable=True),
    sa.Column('room', sa.String(length=120), nullable=True),
    sa.Column('satisfaction', sa.String(length=120), nullable=True),
    sa.Column('chat', sa.String(length=120), nullable=True),
    sa.Column('last_message_read_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=True),
    sa.Column('recipient_id', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['recipient_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_timestamp'), 'message', ['timestamp'], unique=False)
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.Float(), nullable=True),
    sa.Column('payload_json', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_name'), 'notification', ['name'], unique=False)
    op.create_index(op.f('ix_notification_timestamp'), 'notification', ['timestamp'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('language', sa.String(length=5), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    op.create_table('task',
    sa.Column('id', sa.String(length=36), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('complete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_task_name'), 'task', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_task_name'), table_name='task')
    op.drop_table('task')
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_notification_timestamp'), table_name='notification')
    op.drop_index(op.f('ix_notification_name'), table_name='notification')
    op.drop_table('notification')
    op.drop_index(op.f('ix_message_timestamp'), table_name='message')
    op.drop_table('message')
    op.drop_table('followers')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_chat_timestamp'), table_name='chat')
    op.drop_table('chat')
    # ### end Alembic commands ###
