import json
from aiohttp import web

app = web.Application()

def get_data():
    f = open("./data/data.json", "r+")
    data = json.loads(f.read())
    f.close()
    return data