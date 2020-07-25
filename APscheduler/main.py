"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/16-11:26
"""
import time
from APscheduler.task import scheduler
from APscheduler import jobs
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR



# scheduler.add_job(func=jobs.warning, args=("fool1", 'fool2'), trigger='interval', seconds=2, id="15")
# # scheduler.add_job(func=jobs.cancel, args=(scheduler,), trigger='interval', seconds=2)
#
#
# scheduler.add_job(func=jobs.warning, args=("fool3", 'fool4'), trigger='interval', seconds=2, id="14")
scheduler.remove_job("15")

while True:
    time.sleep(5)