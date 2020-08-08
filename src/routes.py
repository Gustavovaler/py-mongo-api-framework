from aiohttp import web
from controllers.Usuarios import UsuariosController

usuarios = UsuariosController()

r = [
    web.get('/', usuarios.handle),
    web.get('/users', usuarios.handle),
    web.post('/', usuarios.handle)
    ]