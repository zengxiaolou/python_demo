"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/15-16:13
"""
from concurrent.futures.thread import ThreadPoolExecutor

from apscheduler.schedulers.background import BlockingScheduler

# 创建定时任务的调度器对象
scheduler = BlockingScheduler()
# 创建执行器
executors = {
    'default': ThreadPoolExecutor(20),
}
# 定义定时任务
def my_job():  # 参数通过add_job()args传递传递过来
    print(1)  # 100
    print(2)  # python

# 向调度器中添加定时任务
scheduler.add_job(my_job, 'interval', seconds=5)

# 启动定时任务调度器工作
scheduler.start()

