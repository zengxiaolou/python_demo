"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/15-16:43
"""
import time
from apscheduler.schedulers.blocking import BlockingScheduler

schedulers = BlockingScheduler


def my_job():
    print(1123)


job = schedulers.add_job(my_job, 'interval', minutes=2)
job.remove()
