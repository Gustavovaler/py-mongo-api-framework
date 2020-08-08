from core.handler import Controller
import asyncio
from core.app import get_data


class UsuariosController(Controller):
    def __init__(self):
        super().__init__()

    async def m_get(self):
        return self.web.json_response(get_data())


    