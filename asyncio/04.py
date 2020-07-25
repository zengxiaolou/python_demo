"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/6-17:07
"""

import asyncio


async def nested():
    return 42


async def main():
    nested()
    print(await nested())

asyncio.run(main())

