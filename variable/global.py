"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/6/16-13:58
"""


def test():
    global a
    print(a)
    a = a + 1


if __name__ == "__main__":
    a = 3
    test()
    print(a)
    test()
