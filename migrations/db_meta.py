from .base import sql_ops


@sql_ops
class DBMeta:
    upgrade = ['create']

    @staticmethod
    def create():
        return '''
        create table if not exists db_meta (
            "id"         serial primary key,
            "table_name" varchar(64),
            "fake"       bool default false
        )'''
