import pathlib
import os

from backend.views import index


PROJECT_ROOT = pathlib.Path(os.getenv('PYTHONPATH', __file__))


def setup_routes(app):
    app.router.add_get('/', index)
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
