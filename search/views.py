from django.shortcuts import render

# Create your views here.

import json
from django.views.generic.base import View
from django.http import HttpResponse
from search.models import tgbusType

class SearchSuggest(View):
    def get(self, request):
        keywds = request.GET.get('s', '')
        returnData = []
        if keywds:
            s = tgbusType.search()
            s.suggest('vonSuggest', keywds, completion={
                "field": "suggestions",
                "fuzzy":{
                    "fuzziness": 3
                },
                "size": 7
            })
            sug = s.execute_suggest()
            for match in sug.vonSuggest[0].options:
                source = match._source
                returnData.append(source["title"])
        return HttpResponse(json.dumps(returnData), content_type="application/json")




from elasticsearch import Elasticsearch
client = Elasticsearch(hosts=["192.168.1.106"])

class SearchView(View):
    def get(self, request):
        keywds = request.GET.get("q", "")
        response = client.search(
            index= "tgbus",
            body={
                "query":{
                    "multi_match":{
                        "query": keywds,
                        "fields":["keywords", "title", "abstract", "content"]

                    }
                },
                "form": 0,
                "size": 13, # 用于分页
                "highlight":{ # 搜索词高亮处理
                    "pre_tags": ['<span  style="color:#A593E0">'],
                    "post_tags": ['</span>'],
                    "fields":{
                        "title":{},
                        "content":{},
                    }
                }
            }
        )
        # 搜索结果总数
        totalNum = response["hits"]["total"]
        hit_list =[]
        for hit in response["hits"]["hits"]:
            hit_dict = {}
            if "title" in hit["highlight"]:
                hit_dict["title"] = "".join(hit["highlight"]["title"])
            else:
                hit_dict["title"] = hit["_source"]["title"]
            if "content" in hit["highlight"]:
                hit_dict["content"] = "".join(hit["highlight"]["content"])[:300]
            else:
                hit_dict["content"] = hit["_source"]["content"][:300]

            hit_dict["author"] = hit["_source"]["author"]
            hit_dict["pubTime"] = hit["_source"]["pubTime"]
            hit_dict["url"] = hit["_source"]["url"]
            hit_dict["score"] = hit["_score"]

            hit_list.append(hit_dict)

        return render(request, "result.html", {"all_hits": hit_list, "keywds":keywds})
