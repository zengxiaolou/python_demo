"""
AUTHOR:  zeng_xiao_yu
GITHUB:  https://github.com/zengxiaolou
EMAIL:   zengevent@gmail.com
TIME:    2020/7/15-17:31
"""
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["192.168.44.163:9200"])

data = {
    "doc": {
        "aa": 3
    }

}

# res = es.index("test1", data)
res = es.update("test1", "mGvaUXMBXRTZYmk_mjaJ", data)

print(res)