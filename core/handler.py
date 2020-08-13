from aiohttp import web


class Controller:
    """
        self.web = aiohttp.web  
        Rewrite index, store, update, delete, show methods into 
            your controller class.
    """
    def __init__(self):
        self.web = web        

    async def index(self, request):
        return self.web.json_response(self.model.all())

    async def update(self, request):
        return self.web.json_response({"method":request.method})

    async def store(self, request):
        
        return self.web.json_response({"method":request.method})

    async def delete(self, request):
        return self.web.json_response({"method":request.method})
    
    async def show(self, request):        
        return self.web.json_response(request.match_info)