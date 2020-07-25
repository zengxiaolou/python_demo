"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/6-15:30
"""
import asyncio


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

# main()
asyncio.run(main())