"""empty message

Revision ID: 50df6c615715
Revises: c64ad9c3db28
Create Date: 2023-02-10 19:34:03.394021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50df6c615715'
down_revision = 'c64ad9c3db28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.drop_constraint('books_author_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.create_unique_constraint('books_author_key', ['author'])

    # ### end Alembic commands ###
