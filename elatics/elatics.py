from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=["192.168.44.163:9200"])

# doc = {
#     'author': 'kimchy',
#     'text': 'Elasticsearch: cool. bonsai cool.',
#     'timestamp': datetime.now(),
# }
#
# res = es.index(index="test-index", id=1, body=doc)
# print(res['result'])
#
# res = es.get(index="test-index", id=1)
# print(res)
#
# es.indices.refresh(index="test-index")
# body = {
#     "size": "1",
#     "aggs": {
#         "max_balance": {
#             "avg": {
#                 "field": "v.free_cpu_usage"
#             }
#         }
#     }
# }
data = {
    "aa": 1,
    "vv": 3,
    "xx":  3,
}


actions = [
            {"update": {"_index": "test1", "_type": "_doc", "_id": "09a9d942-c9b3-4de5-8953-f61bac9617"}},
            {"doc": data, "upsert": data}
            # {"index": {"_index": "current_cpu_usage_avg", "_type": "_doc"}},
            # {"test": "1"}
    ]
res = es.bulk(actions)
print(res)

# print("Got %d Hits:" % res['hits']['total']['value'])
# for hit in res['hits']['hits']:
#     print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])