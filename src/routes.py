from aiohttp import web
from controllers.Usuarios import UsuariosController
from controllers.Productos import ProductosController

    
r = [
    web.get('/users/', UsuariosController().index),
    web.get('/products', ProductosController().index)
   
    ]