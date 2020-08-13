from aiohttp import web
from controllers.Usuarios import UsuariosController
from controllers.Productos import ProductosController
from controllers.Doctors import DoctorsController
    
urls = [
    web.get('/api/v1/users', UsuariosController().index),
    web.get('/api/v1/users/{nombre}', UsuariosController().show),
    web.post('/api/v1/users', UsuariosController().store),
    web.get('/api/v1/products', ProductosController().index),
    web.post('/api/v1/products', ProductosController().store),
    web.get('/api/v1/products/{modelo}', ProductosController().show),
    web.post('/api/v1/doctors', DoctorsController().store),
    web.get('/api/v1/doctors', DoctorsController().index)
   
    ]