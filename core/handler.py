from aiohttp import web
from .app import get_data


class Controller:
    """
        self.web = aiohttp.web  
        Rewrite index, store, update, delete, show mothods into 
            your controller class.
    """
    def __init__(self):
        self.web = web        

    async def index(self, request):
        return self.web.json_response({"method":request.method})

    async def update(self, request):
        return self.web.json_response({"method":request.method})

    async def store(self, request):
        
        return self.web.json_response({"method":request.method})

    async def delete(self, request):
        return self.web.json_response({"method":request.method})
    
    async def show(self, request):
        return self.web.json_response({"method":request.method})