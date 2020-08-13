from core.handler import Controller
from models import productos
import asyncio



class ProductosController(Controller):

    def __init__(self):
        super().__init__()
        self.model = productos.Producto()
        self.model.set_collection("products")

