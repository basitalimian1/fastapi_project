"""Add content column to post table

Revision ID: c997a96ea09d
Revises: bcb2f25e5404
Create Date: 2023-03-30 16:06:28.996899

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c997a96ea09d'
down_revision = 'bcb2f25e5404'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade() -> None:
    op.drop_column('posts','content')
    pass
