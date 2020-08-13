from core.handler import Controller
from models import usuarios
import asyncio



class UsuariosController(Controller):
    """
    method  index(self, request)
    method  show(self, request)
    method  update(self, request)
    method  delete(self,request)
    method  store(self, request)

    """

    def __init__(self):
        super().__init__()
        self.model = usuarios.Usuario()
        self.model.set_collection("users")

    def show(self, request):
        data = self.model.find_one(request.match_info)
        return self.web.json_response(data)

    

    
    