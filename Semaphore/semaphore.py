"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/6/25-17:45
"""
import random
import time
from multiprocessing import Process, Semaphore


def go_wc(sem: Semaphore(), user: str):
    sem.acquire()
    print(f'{user}占到一个茅坑')
    time.sleep(random.randint(0, 3))  # 模拟每个人拉屎的速度不一样，0表示有的人蹲下就起来
    sem.release()


if __name__ == '__main__':
    sem = Semaphore(2)
    p_l = []
    for i in range(10):
        p = Process(target=go_wc, args=(sem, f'user{i}'))
        p.start()
        p_l.append(p)

    for i in p_l:
        i.join()
        print("=" * 30)
