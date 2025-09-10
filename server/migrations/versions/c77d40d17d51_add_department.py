from alembic import op
import sqlalchemy as sa

def upgrade():
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    if "departments" not in inspector.get_table_names():
        op.rename_table("department", "departments")

def downgrade():
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    if "department" not in inspector.get_table_names():
        op.rename_table("departments", "department")
