"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/6-15:59
"""
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f'start at {time.strftime("%X")}')

    await say_after(1, 'hello')
    await say_after(1, 'world')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())