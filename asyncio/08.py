"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/7-15:22
"""
from elasticsearch import Elasticsearch
import datetime


es = Elasticsearch(hosts=["192.168.44.163:9200"])
query = {
    "_source": ['v', 'tm', 'ne'],
    "aggs": {
        "ne_id": {
            "terms": {
                "field": "ne"
            },
            "aggs": {'data_sum': {'sum': {'field': 'v.used_cpu_usage'}}}
        }
    }
}
es_data = es.search(query, index="current_cpu_usage_core", doc_type='_doc')
aggregations_data = es_data["aggregations"]["ne_id"]["buckets"]
_id = "day" + "_" + "used_cpu_usage" + "_" + str(int(datetime.datetime.now().timestamp() * 1000))
# body = {
#     "indicator": "cpu_usage_core",
#     "attr": "used_cpu_usage",
#     "begin_time": int(datetime.datetime.now().timestamp() * 1000),
#     "end_time": int(datetime.datetime.now().timestamp() * 1000),
#     "add_time": int(datetime.datetime.now().timestamp() * 1000),
#     "aggregation_result": aggregations_data
# }
body = {
    "indicator": "cpu_usage_core",
    "attr": "used_cpu_usage"}
es.index(index="aggregation_cpu_usage_core", id=1, body=body)
