"""threads_posts

Revision ID: 1c8abec8f9f9
Revises: f386c9e48425
Create Date: 2019-12-16 17:17:26.584959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1c8abec8f9f9"
down_revision = "f386c9e48425"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "misago_posts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("thread_id", sa.Integer(), nullable=False),
        sa.Column("poster_id", sa.Integer(), nullable=True),
        sa.Column("poster_name", sa.String(length=255), nullable=False),
        sa.Column("body", sa.JSON(), nullable=False),
        sa.Column("edits", sa.Integer(), nullable=False),
        sa.Column("posted_at", sa.DateTime(), nullable=False),
        sa.Column("extra", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(["category_id"], ["misago_categories.id"],),
        sa.ForeignKeyConstraint(
            ["poster_id"], ["misago_users.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(["thread_id"], ["misago_threads.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "misago_threads",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("first_post_id", sa.Integer(), nullable=True),
        sa.Column("starter_id", sa.Integer(), nullable=True),
        sa.Column("starter_name", sa.String(length=255), nullable=False),
        sa.Column("last_poster_id", sa.Integer(), nullable=True),
        sa.Column("last_poster_name", sa.String(length=255), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("slug", sa.String(length=255), nullable=False),
        sa.Column("started_at", sa.DateTime(), nullable=False),
        sa.Column("last_posted_at", sa.DateTime(), nullable=False),
        sa.Column("replies", sa.Integer(), nullable=False),
        sa.Column("is_closed", sa.Boolean(), nullable=False),
        sa.Column("extra", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(["category_id"], ["misago_categories.id"],),
        sa.ForeignKeyConstraint(
            ["first_post_id"], ["misago_posts.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["last_poster_id"], ["misago_users.id"], ondelete="SET NULL"
        ),
        sa.ForeignKeyConstraint(
            ["starter_id"], ["misago_users.id"], ondelete="SET NULL"
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "misago_threads_order",
        "misago_threads",
        [sa.text("last_posted_at DESC"), "category_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("misago_threads_order", table_name="misago_threads")
    op.drop_table("misago_threads")
    op.drop_table("misago_posts")
    # ### end Alembic commands ###
