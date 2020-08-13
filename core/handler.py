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
        data = await request.post()
        keys =  [d for d in data ]
        document = {}
        for key in keys:
            document[key] = data[key]        
        self.model.insert_one(document)
        return self.web.json_response({})

    async def delete(self, request):
        return self.web.json_response({"method":request.method})
    
    async def show(self, request):
        data = self.model.find_one(request.match_info)
        return self.web.json_response(data)