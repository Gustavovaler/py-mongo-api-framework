from aiohttp import web
from .app import get_data


class Controller:
    """
        self.web = aiohttp.web  
        Rewrite m_get, m_post, m_update, m_delet mothods into 
            your controller class.
    """
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

    async def m_get(self):
        return

    async def m_post(self):
        return

    async def m_update(self):
        return

    async def m_delete(self):
        return
    