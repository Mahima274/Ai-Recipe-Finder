"""Update leave_type column in LeaveRequest model

Revision ID: cd17d4630645
Revises: cd17d4630644
Create Date: 2025-01-31 21:30:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd17d4630645'
down_revision = 'cd17d4630644'
branch_labels = None
depends_on = None


def upgrade():
    # Update the leave_type column to be non-nullable
    with op.batch_alter_table('leave_request', schema=None) as batch_op:
        batch_op.alter_column('leave_type', nullable=False)


def downgrade():
    # Revert the leave_type column to be nullable
    with op.batch_alter_table('leave_request', schema=None) as batch_op:
        batch_op.alter_column('leave_type', nullable=True)
