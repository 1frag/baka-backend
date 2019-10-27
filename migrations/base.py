relations = []


def sql_ops(cls):

    async def go(engine, ops):
        async with engine.acquire() as conn:
            for name_fun in ops:
                op = getattr(cls, name_fun)()
                await conn.execute(op)
                print(f'{name_fun} in {cls.__name__} done')

    async def up(engine):
        await go(engine, cls.upgrade)

    async def down(engine):
        await go(engine, cls.downgrade)

    class Wrapper(cls):
        pass

    Wrapper.up = up
    Wrapper.down = down
    relations.append(Wrapper)

    return Wrapper
