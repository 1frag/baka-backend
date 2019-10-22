import os


SETTINGS = {
    'postgres': dict(
        database='postgres',
        user='postgres',
        password='postgres',
        host='db',
        port=5432,
    ),
}


if os.getenv('PRODUCTION'):
    SETTINGS.update({
        'postgres': {'dsn': os.getenv('DATABASE_URL')},
    })
