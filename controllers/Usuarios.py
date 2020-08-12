from core.handler import Controller
from models import usuarios
import asyncio



class UsuariosController(Controller):

    def __init__(self):
        super().__init__()
        self.model = usuarios.Usuario()
        self.model.set_collection("users")

    def index(self, request):        
        return  self.web.json_response(self.model.all())

    
    