import asyncio, time
from aiolimiter import AsyncLimiter


RATE_LIMIT = 10 # max_rate
QTD = 1
limiter = AsyncLimiter(max_rate=RATE_LIMIT)

def show_time() -> str:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

async def create_task(num):
    global QTD
    async def execute_task(id):
        global QTD
        await asyncio.sleep(5)
        print(f'RUN: ({id:>2d}) ', show_time(), f' Count: {QTD:>2d} Drip! {time.time() - ref:>5.2f}')
        QTD += 1

    print(f'CREATE ({num:>2d}) ', show_time())

    async with limiter:
        print(f'Start ({num:>2d}) ', show_time())
        await execute_task(num)
        print(f'END ({num:>2d}) ', show_time())

if __name__ == "__main__":
    print("main ok")
    tasks = [create_task(i) for i in range(100)]
    ref = time.time()
    result = asyncio.run(asyncio.wait(tasks))
