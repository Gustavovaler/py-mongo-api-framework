from aiohttp import web
from .app import get_data

class Controller:
    def __init__(self):
        self.web = web

    async def handle(self,request):
        self.request = request
        if request.method == 'GET':
            process = await self.m_get()
            return process
        if request.method == 'POST':
            m =  request.content
            print(await m.readany())
            return self.web.json_response({"saved":True})

    