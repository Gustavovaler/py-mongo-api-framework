from core.handler import Controller
from models import doctors
import asyncio



class DoctorsController(Controller):
    """
    method  async index(self, request)
    method  async show(self, request)
    method  async update(self, request)
    method  async delete(self,request)
    method  async store(self, request)

    """

    def __init__(self):
        super().__init__()
        self.model = doctors.Doctor()
        self.model.set_collection("doctors")