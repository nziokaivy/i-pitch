"""fifth migration

Revision ID: d97551d9938b
Revises: 671529a5fcb0
Create Date: 2019-02-12 15:52:15.046848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd97551d9938b'
down_revision = '671529a5fcb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=False))
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###
