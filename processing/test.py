"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/6/26-15:50
"""
import os
from multiprocessing import process, current_process


def doubler(number: int):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    print('proc_id:{0} proc_name:{1} result:{2}'.format(proc_id, proc_name, result))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []
    for num in numbers:
        pass
