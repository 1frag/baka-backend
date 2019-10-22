import asyncio

import sqlalchemy as sa
from utils import get_engine

metadata = sa.MetaData()


async def create_table(engine):
    async with engine.acquire() as conn:
        await conn.execute('drop table e_user;')
        await conn.execute('''
            CREATE TABLE e_user
            (
                id         int8        not null,
                name       varchar(64) not null,
                started_at date        default now(),
                PRIMARY KEY (id)
            );
        ''')


async def go():
    async with get_engine() as engine:
        await create_table(engine)


loop = asyncio.get_event_loop()
loop.run_until_complete(go())
