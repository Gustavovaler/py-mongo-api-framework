from aiohttp import web
from controllers.Usuarios import UsuariosController
from controllers.Productos import ProductosController

    
urls = [
    web.get('/api/v1/users', UsuariosController().index),
    web.get('/api/v1/users/{nombre}', UsuariosController().show),
    web.post('/api/v1/users', UsuariosController().store),
    web.get('/api/v1/products', ProductosController().index)
   
    ]