"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/15-16:37
"""
import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()


@scheduler.scheduled_job("interval", seconds=5)
def my_job():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))


scheduler.start()