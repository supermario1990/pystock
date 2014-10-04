"""Added more models

Revision ID: 2c08fb5b6e72
Revises: 3bfca079f84d
Create Date: 2014-09-01 00:01:51.077215

"""

# revision identifiers, used by Alembic.
revision = '2c08fb5b6e72'
down_revision = '4ee9a9c23b8f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ## commands auto generated by Alembic - please adjust! ###
    op.add_column(u'pystock_fxrates', sa.Column('created_on', sa.DateTime(), nullable=False))

    op.create_table('pystock_user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pystock_book',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['pystock_user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )

    op.create_table('pystock_exchange',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('code', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    op.add_column(u'pystock_security', sa.Column('exchange_id', sa.Integer(), nullable=True))

    op.create_table('pystock_liability',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pystock_company',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_constraint(None, 'pystock_currency')
    op.drop_column(u'pystock_fxrates', sa.Column('created_on', sa.DateTime(), nullable=True))
    op.drop_table('pystock_book')
    op.drop_table('pystock_user')
    op.drop_table('pystock_exchange')
    op.drop_table('pystock_liability')
    op.drop_table('pystock_company')
