"""add index to origin

Revision ID: 7baeb95b92d3
Revises: 9fc0ea4d0c23
Create Date: 2019-02-24 16:10:52.702458

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7baeb95b92d3'
down_revision = '9fc0ea4d0c23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_url_origin'), 'url', ['origin'], unique=True)
    op.drop_constraint('url_origin_key', 'url', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('url_origin_key', 'url', ['origin'])
    op.drop_index(op.f('ix_url_origin'), table_name='url')
    # ### end Alembic commands ###