"""empty message

Revision ID: a875403eb27c
Revises: 
Create Date: 2023-02-10 01:46:01.770646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a875403eb27c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book_genres',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=120), nullable=False))
        batch_op.alter_column('author',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=120),
               existing_nullable=False)
        batch_op.alter_column('publication_date',
               existing_type=sa.DATE(),
               nullable=False)
        batch_op.drop_column('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('books', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
        batch_op.alter_column('publication_date',
               existing_type=sa.DATE(),
               nullable=True)
        batch_op.alter_column('author',
               existing_type=sa.String(length=120),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)
        batch_op.drop_column('title')

    op.drop_table('book_genres')
    op.drop_table('genres')
    # ### end Alembic commands ###
