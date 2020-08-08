from aiohttp import web
from controllers.Usuarios import UsuariosController
from controllers.Index import IndexController



    
r = [
    web.get('/',IndexController().index),
    web.get('/users/{numero}', UsuariosController().index),
    web.post('/', IndexController().store)
    ]