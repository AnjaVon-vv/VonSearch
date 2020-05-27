from django.test import TestCase

# Create your tests here.
from elasticsearch import Elasticsearch

s = Elasticsearch()
s.search(index='tgbus', )

