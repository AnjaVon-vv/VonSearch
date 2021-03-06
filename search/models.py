from django.db import models

# Create your models here.

__author__ = 'Von'

from elasticsearch_dsl import DocType, Date, Completion, Keyword, Text

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["192.168.1.106"])
# config/.yml --> network --> ip

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}
ikAnalyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class tgbusType(DocType):
    # 为type创建mapping
    suggestion = Completion(analyzer=ikAnalyzer)
    title = Text(analyzer="ik_max_word")
    author = Keyword()
    keywords = Keyword()
    abstract = Text()
    pubTime = Date()
    content = Text(analyzer="ik_max_word")
    url = Keyword()

    class Meta:
        index = "tgbus"
        doc_type = "article"

# 根据type生成mapping
if __name__ == "__main__":
    tgbusType.init()