import aiohttp_jinja2
from aiohttp import web

import db


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.user.select())
        records = await cursor.fetchall()
        # questions = [dict(q) for q in records]
        return {'records': records}
