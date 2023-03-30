"""Create posts table

Revision ID: bcb2f25e5404
Revises: 
Create Date: 2023-03-30 15:46:13.318322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcb2f25e5404'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title', sa.String(), nullable =False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
