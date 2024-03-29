import pathlib
import os

from backend.views import index, content


PROJECT_ROOT = pathlib.Path(os.getenv('PYTHONPATH', __file__))


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/content', content, name='content')
    setup_static_routes(app)


def setup_static_routes(app):
    app.router.add_static('/app/static/' if os.getenv('PRODUCTION') else '/static/',
                          path=PROJECT_ROOT / 'static',
                          name='static')
