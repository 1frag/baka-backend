import trafaret as T
from settings import SETTINGS
from aiopg.sa import create_engine


TRAFARET = T.Dict({
    T.Key('postgres'):
        T.Dict({
            'database': T.String(),
            'user': T.String(),
            'password': T.String(),
            'host': T.String(),
            'port': T.Int(),
            'minsize': T.Int(),
            'maxsize': T.Int(),
        }),
    T.Key('host'): T.IP,
    T.Key('port'): T.Int(),
})


def get_db():
    conf = SETTINGS['postgres']
    if conf.get('dsn'):
        return conf['dsn']
    else:
        return 'postgres://{user}:{password}@{host}:{port}/{database}'.format(**conf)


def get_engine():
    return create_engine(dsn=get_db())
