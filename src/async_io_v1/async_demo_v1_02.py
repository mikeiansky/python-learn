import asyncio
import time

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    # time.sleep(3)
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')
    print('main complete')

asyncio.run(main())