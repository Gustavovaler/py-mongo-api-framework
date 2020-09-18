from aiohttp import web
from controllers.Usuarios import UsuariosController
from controllers.Productos import ProductosController
from controllers.Doctors import DoctorsController
from core.handler import Controller


    
urls = [

    web.view('/api/v1/users', UsuariosController),
    # web.get('/api/v1/users/{nombre}', UsuariosController().show),
    # web.post('/api/v1/users', UsuariosController().store),
    # web.delete('/api/v1/users/{id}', UsuariosController().delete),
    # web.get('/api/v1/products', ProductosController().index),
    # web.post('/api/v1/products', ProductosController().store),
    # web.get('/api/v1/products/{id}', ProductosController().show),
    # web.post('/api/v1/doctors', DoctorsController().store),
    # web.get('/api/v1/doctors', DoctorsController().index),
    # web.delete('/api/v1/doctors/{id}', DoctorsController().delete)
   
    ]

