import aiopg.sa
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)
import datetime

__all__ = ['user']

meta = MetaData()

user = Table(
    'e_user', meta,

    Column('id', Integer, primary_key=True),
    Column('name', String(64), nullable=False),
    Column('started_at', Date, nullable=False, default=datetime.datetime.utcnow)
)


async def init_pg(app):
    engine = await aiopg.sa.create_engine(
        **app['config']['postgres']
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
