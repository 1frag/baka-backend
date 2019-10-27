import aiohttp_jinja2

from backend import db


@aiohttp_jinja2.template('index.html')
async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.user.select())
        records = await cursor.fetchall()
        # questions = [dict(q) for q in records]
        return {'records': records}


@aiohttp_jinja2.template('content.html')
async def content(request):
    return {}
