from core.handler import Controller


class IndexController(Controller):

    def __init__(self):
        super().__init__()

    async def index(self, request):
        return self.web.json_response({"method": request.method})
    