from aiohttp import web
from controllers.Usuarios import UsuariosController
from controllers.Productos import ProductosController

    
r = [
    web.get('/api/v1/users', UsuariosController().index),
    web.get('/api/v1/users/{id}', UsuariosController().show),
    web.get('/products', ProductosController().index)
   
    ]