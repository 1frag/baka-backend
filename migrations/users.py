from migrations.base import sql_ops


@sql_ops
class Users:
    upgrade = ['drop', 'create']

    @staticmethod
    def drop():
        return 'drop table if exists e_user;'

    @staticmethod
    def create():
        return '''create table e_user (
            id         serial primary key,
            name       varchar(16) unique,
            created_at date default now()::date
        );'''
