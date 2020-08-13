from .app import app
from src.routes import urls

routes = app.add_routes(urls)

