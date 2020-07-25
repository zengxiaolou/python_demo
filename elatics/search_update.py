"""
AUTHOR:         zeng_xiao_yu
GITHUB:         https://github.com/zengxiaolou
EMAIL:          zengevent@gmail.com
TIME:           2020/7/16-17:33
INSTRUCTIONS:   测试查询更新
"""
from elasticsearch import Elasticsearch
import time

es = Elasticsearch(hosts=["192.168.44.163:9200"])

tm = int(time.time() * 1000)
data = {
    "query": {
        "bool": {
            "must": [
                {"match": {"ne": "6c9353d0-2b72-4803-9ed4-106df40bca70"}},
                {"range": {
                    "tm": {
                        "lte": tm
                    }}}
            ],
            "must_not": [
                {"match": {
                    'runStatus': "Back"}}]
        }
    },
    "script": {
        "inline": "ctx._source.runStatus=params.status",
        "params": {
            "status": "Backe"
        },
        "lang": "painless"
    }

}

# res = es.index("test1", data)
res = es.update_by_query("monitor_history_cpu_usage_avg", body=data)

print(res)
