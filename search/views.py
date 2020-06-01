# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.
# __author__: 'Von'


# class IndexView(View):
#     # 首页top3
#     def get(self, request):
#         top3Search = redisClient.zrevrangebyscore("keywdsCnt", "+inf", "-inf", start=0, num=3)
#         return render(request, "index.html", {"top3Search": top3Search})



import json
from django.http import HttpResponse
from search.models import tgbusType

class SearchSuggest(View):
    def get(self, request):
        keywds = request.GET.get('s', '')
        returnData = []
        if keywds:
            s = tgbusType.search()
            s = s.suggest('vonSuggest', keywds, completion={
                "field": "suggestion",
                "fuzzy":{
                    "fuzziness": 3
                },
                "size": 7
            })
            sug = s.execute()
            for match in sug.suggest.vonSuggest[0].options:
                source = match._source
                returnData.append(source["title"])
        return HttpResponse(json.dumps(returnData), content_type="application/json")




from elasticsearch import Elasticsearch
client = Elasticsearch(hosts=["192.168.1.106"])


from datetime import datetime

class SearchView(View):
    def get(self, request):
        keywds = request.GET.get("q", "")

        # redisClient.zincrby("keywdsCnt", 1, keywds)
        # top3Search = redisClient.zrevrangebyscore("keywdsCnt", "+inf", "-inf", start=0, num=3)


        page = request.GET.get("p", "1")
        try:
            page = int(page)
        except:
            page = 1

        tgbusCnt = 9997
        # import redis
        # redisClient = redis.StrictRedis(host='192.168.1.106')
        # tgbusCnt = redisClient.get("tgbusCnt")

        startTime = datetime.now()
        response = client.search(
            index= "tgbus",
            body={
                "query":{
                    "multi_match":{
                        "query": keywds,
                        "fields":["keywords", "title", "abstract", "content"]
                    }
                },
                "sort": [
                    {
                        "PR": {
                            "order": "desc"
                        }
                    }
                ],
                "from": (page - 1) * 13,
                "size": 13, # 用于分页
                "highlight":{ # 搜索词高亮处理
                    "pre_tags": ['<span  style="color:#A593E0">'],
                    "post_tags": ['</span>'],
                    "fields":{
                        "title": {},
                        "content": {},
                    }
                }
            }
        )
        # 搜索结果总数
        endTime = datetime.now()
        lastTime = (endTime - startTime).total_seconds()
        totalNum = response["hits"]["total"]
        if(page%13) > 0:
            pageNum = int(totalNum/13 + 1)
        else:
            pageNum = int(totalNum/13)
        hit_list =[]
        for hit in response["hits"]["hits"]:
            hit_dict = {}
            if "highlight" in hit:
                if "title" in hit["highlight"]:
                    hit_dict["title"] = "".join(hit["highlight"]["title"])
                else:
                    hit_dict["title"] = hit["_source"]["title"]

                if "content" in hit["highlight"]:
                    hit_dict["content"] = "".join(hit["highlight"]["content"])[:300]
                else:
                    hit_dict["content"] = hit["_source"]["content"][:300]
            else:
                hit_dict["content"] = hit["_source"]["content"][:300]
                hit_dict["title"] = hit["_source"]["title"]

            hit_dict["author"] = hit["_source"]["author"]
            hit_dict["pubTime"] = hit["_source"]["pubTime"]
            hit_dict["url"] = hit["_source"]["url"]
            hit_dict["PR"] = hit["_source"]["PR"]

            hit_list.append(hit_dict)

        return render(request, "result.html", {"page": page,
                                           "all_hits": hit_list,
                                           "keywds": keywds,
                                           "totalNum": totalNum,
                                           "lastNum": lastTime,
                                           "tgbusCnt": tgbusCnt,})
                                           # "top3Search": top3Search})
