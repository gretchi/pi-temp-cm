"""create_table

Revision ID: b8b60d090244
Revises:
Create Date: 2022-05-20 17:56:40.754534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8b60d090244'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("CREATE SEQUENCE temperature_id_seq;")

    conn.execute(
        """CREATE TABLE temperature (
        id INT NOT NULL DEFAULT nextval('temperature_id_seq'),
        mac VARCHAR(32) NOT NULL,
        temp FLOAT NOT NULL,
        humidity FLOAT NOT NULL,
        battery INT NOT NULL,
        sent_at TIMESTAMP NOT NULL,
        create_at TIMESTAMP NULL DEFAULT now(),
        PRIMARY KEY (id));
    """
    )


def downgrade():
    conn = op.get_bind()
    conn.execute("DROP TABLE temperature;")
    conn.execute("DROP SEQUENCE temperature_id_seq;")
