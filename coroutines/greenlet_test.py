"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/5/19-03:48
"""
from greenlet import greenlet


def func1():
    print(1)
    gr2.switch()
    print(2)
    gr2.switch()


def func2():
    print(3)
    gr1.switch()
    print(4)


gr1 = greenlet(func1)
gr2 = greenlet(func2)
gr1.switch()
