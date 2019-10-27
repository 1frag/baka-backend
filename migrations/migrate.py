import asyncio
import sys

from backend.utils import get_engine
from migrations.base import relations


async def go(*args):
    if args[0] in ['upgrade', 'downgrade']:
        op = 'up' if args[0] == 'upgrade' else 'down'

        async with get_engine() as engine:
            for table in relations:
                await getattr(table, op)(engine)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(go(*sys.argv[1:]))
