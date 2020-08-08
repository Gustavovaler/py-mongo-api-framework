from .app import app
from src.routes import r

routes = app.add_routes(r)

