import aiohttp, asyncio, time
from aiolimiter import AsyncLimiter

"""
def get_sync2(name):
    print(show_time(), f'Start {name} -', end=' ')
    coro = fetch(URL)
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(coro)
    ref = time.time()
    print(show_time(), f'End {name} - time: {time.time() - ref:>5.2f}')

def main_sync2():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[async_exec(get_sync2(i)) for i in range(MAX_CLIENTS)]))
"""

RATE_LIMIT = 2
MAX_CLIENTS = 10
limiter = AsyncLimiter(max_rate=RATE_LIMIT, time_period=10)
URL = 'https://api.github.com/events'


def show_time() -> str:
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

async def fetch(url):
    async with aiohttp.ClientSession(trust_env=True) as session:
        async with session.get(url) as response:
            return await response.json()

def sync_exec(coro):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coro)

async def async_exec(func, *args):
        return await func(args)

def get_sync(name, ref):
    print(show_time(), f'Start {name} -', end=' ')
    coro = fetch(URL)
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(coro)
    print(show_time(), f'End {name} - time: {time.time() - ref:>5.2f}')

async def get_async(name):
    print(show_time(), f'>> Start {name} -')
    await fetch(URL)
    print(show_time(), f'<< End {name} - Time: {time.time() - ref:>5.2f}')

def main_sync():
    for i in range(MAX_CLIENTS):
        ref = time.time()
        get_sync(i, ref)

if __name__ == "__main__":
    # main_sync()
    requests = [get_async(i) for i in range(MAX_CLIENTS)]
    ref = time.time()
    # asyncio.run(asyncio.wait(requests))

    # RUN 2 asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*requests))
