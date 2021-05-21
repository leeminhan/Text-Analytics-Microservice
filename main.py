from typing import Optional
from fastapi import FastAPI
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

app = FastAPI()
client = Elasticsearch()
# configure analyzer

from elasticsearch_dsl import connections
connections.create_connection(hosts=['localhost'], timeout=20)

@app.get("/")
def read_root():
    return {"Hello": "World"}
