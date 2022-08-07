"""migration

Revision ID: cd94ebe9b823
Revises: 474d2b93458f
Create Date: 2022-08-07 23:24:06.397935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd94ebe9b823'
down_revision = '474d2b93458f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('detections', 'confidence')
    op.drop_column('posts', 'system_validated')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('system_validated', sa.BOOLEAN(), nullable=True))
    op.add_column('detections', sa.Column('confidence', sa.FLOAT(), nullable=False))
    # ### end Alembic commands ###
