"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/16-11:19
"""


def warning(x, y):
    print(x)
    print(y)


def cancel(x):
    x.remove_job('11')
    print('任务删除')

