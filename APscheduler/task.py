"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/16-15:19
"""
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor



job_stores = {
    "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}
executors = {
    'default': ThreadPoolExecutor(20),
    'process_pool': ProcessPoolExecutor(10)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_defaults=job_defaults)

scheduler.start()