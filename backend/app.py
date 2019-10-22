import logging
import sys

import aiohttp_jinja2
from jinja2 import FileSystemLoader
from aiohttp import web

from backend.db import close_pg, init_pg
from backend.routes import setup_routes
from backend.settings import SETTINGS


async def init_app(argv=None):

    app = web.Application()

    app['config'] = SETTINGS

    # setup Jinja2 template renderer
    aiohttp_jinja2.setup(
        app, loader=FileSystemLoader('templates'))

    # create db connection on startup, shutdown on exit
    app.on_startup.append(init_pg)
    app.on_cleanup.append(close_pg)

    # setup views and routes
    setup_routes(app)

    return app


def main(argv):
    logging.basicConfig(level=logging.DEBUG)

    app = init_app(argv)

    web.run_app(app, port=argv[0])


if __name__ == '__main__':
    main(sys.argv[1:])
