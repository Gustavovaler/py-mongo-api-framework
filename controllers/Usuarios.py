from core.handler import Controller
from models import usuarios
import asyncio



class UsuariosController(Controller):
    """
    method  async index(self, request)
    method  async show(self, request)
    method  async update(self, request)
    method  async delete(self,request)
    method  async store(self, request)

    """

    def __init__(self):
        self.model = usuarios.Usuario()
        self.model.set_collection("users")


    



    

    
    